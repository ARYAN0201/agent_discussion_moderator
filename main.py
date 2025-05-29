from personas.engineer import engineer_respond
from personas.pm import pm_respond
from personas.designer import designer_respond

from utils.ConversationContext import ContextManager
from utils.moderator_utils import ModeratorUtils

import datetime
import os
from rich.console import Console

console = Console()

def log_to_file(message, filepath="discussion_log.txt", print_to_console=False, style="white"):
    with open(filepath, "a") as f:
        f.write(message + "\n")
    if print_to_console:
        console.print(message, style=style)

def get_response(speaker, question, history):
    if speaker == "Engineer":
        return engineer_respond(question, history)
    elif speaker == "PM":
        return pm_respond(question, history)
    elif speaker == "Designer":
        return designer_respond(question, history)
    else:
        return ""

def main():
    # Setup
    context = ContextManager()
    moderator = ModeratorUtils(max_rounds=10)
    log_file = "discussion_log.txt"

    # Clear previous logs if any
    if os.path.exists(log_file):
        os.remove(log_file)

    log_to_file(f"# Discussion Log - {datetime.datetime.now()}\n", print_to_console=True, style="bold green")

    # Topic input
    question = input("Enter the discussion topic: ")
    context.set_initial_query(question)
    log_to_file(f"🔍 Discussion Topic: {question}\n", print_to_console=True, style="bold blue")

    last_speaker = "Designer"

    # Main discussion loop
    while context.round_count < moderator.max_rounds:
        round_num = context.round_count + 1

        speaker = moderator.select_next_speaker(context.history, last_speaker)
        log_to_file(f"\n🔁 Round {round_num} | 🎙️ Next Speaker: {speaker}", print_to_console=True, style="bold cyan")

        response = get_response(speaker, context.initial_query, "\n".join(context.history))
        log_to_file(f"{speaker}: {response}", print_to_console=True, style="white")

        role_feedback = moderator.check_role_adherence(speaker, response)
        if role_feedback != "Yes, aligns well.":
            mod_note = f"🧭 Moderator Note on Role Alignment: {role_feedback}"
            log_to_file(mod_note, print_to_console=True, style="yellow")

        context.add_message(speaker, response)

        # Conflict detection
        conflict = moderator.detect_conflict("\n".join(context.history))
        if conflict != "None":
            mod_comment = f"⚠️ Moderator Conflict Comment: {conflict}"
            log_to_file(f"Moderator: {conflict}", print_to_console=True, style="bold red")
            context.add_message("Moderator", conflict)

        # Gap detection
        gap = moderator.identify_missing_points("\n".join(context.history))
        if gap != "None":
            gap_comment = f"🔍 Moderator: One area not yet discussed: {gap}"
            log_to_file(gap_comment, print_to_console=True, style="italic green")

        context.update_round()
        last_speaker = speaker

        # Token budget check
        token_status = moderator.check_token_budget(context.round_count)
        log_to_file(f"📏 Token Check: {token_status}", print_to_console=True, style="dim")

        if "⚠️" in token_status:
            log_to_file("🛑 Token limit nearing. Initiating final comment round...\n", print_to_console=True, style="bold red")
            break

    # Final comments
    log_to_file("\n🎤 Final Comments Round", print_to_console=True, style="bold magenta")
    for speaker in ["PM", "Engineer", "Designer"]:
        response = get_response(speaker, context.initial_query, "\n".join(context.history))
        log_to_file(f"{speaker} Final Comment: {response}", print_to_console=True, style="white")
        context.add_message(speaker, response)

    # Final decision summary
    final_summary = moderator.summarize_final_decision("\n".join(context.history), context.initial_query)
    log_to_file("\n📋 Final Decision Summary:", print_to_console=True, style="bold green")
    log_to_file(final_summary, print_to_console=True, style="green")

    print(f"\n✅ Discussion complete. Log saved to `{log_file}`.")

if __name__ == "__main__":
    main()