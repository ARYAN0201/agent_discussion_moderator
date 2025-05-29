conflict_detection = """
        You are a logical observer in a multi-person discussion involving a PM, Software Engineer, and Product Designer.
        Your ONLY job is to detect **actual conflicting or contradicting statements** that have already been made in the conversation.

        Conversation:
        {history}

        Instructions:
        - Only identify **direct contradictions or disagreements** between participants.
        - Do not invent or suggest potential problems that haven't been mentioned.
        - Do not comment on missing points or decisions that should be made.
        - If participants haven't directly disagreed or contradicted each other, respond: None

        Examples:
        - "The engineer wants to launch fast, but the PM is concerned about scalability risks."
        - "The designer pushes for simplicity, while the engineer favors more features."
        - "None"

        Respond only with the summary of the conflict (1 sentence) or 'None':"""

gap_detection = """
        You are a logical and neutral moderator reviewing a strategic product discussion involving a PM, Software Engineer, and Product Designer.
        Your task is to detect **important but missing discussion points** — aspects that should ideally be discussed but haven’t been mentioned yet.
        
        Conversation so far:
        {history}

        Instructions:
        - Do NOT summarize what has been discussed.
        - Instead, list 1–2 important points or questions that have NOT been raised yet.
        - Only include things relevant to product development strategy, design, tech feasibility, business alignment, etc.
        - If all important angles have already been covered, respond with: "None"

        Examples:
        - "Nobody discussed accessibility concerns yet."
        - "The team hasn’t talked about tech stack or performance yet."
        - "None"

        Respond only with the missing discussion points or "None":"""

role_adherence = """
        You are monitoring whether people are sticking to their assigned professional roles in a product meeting.

        Role: {role}
        Response: {response}

        Check if the speaker is focusing on their expected domain.

        Expected Domains:
        - Engineer: software architecture, scalability, technical tradeoffs
        - PM: business goals, delivery timelines, market fit
        - Designer: user experience, interface design, usability

        Respond with:
        - "Yes! aligns well." if the response aligns with the role
        - OR a short sentence if the speaker is going off-topic (e.g., "This seems more like a business concern.")

        Your output:"""

summary_generation = """
        You are a moderator concluding a strategic discussion between a PM, Engineer, and Designer.

        Topic of Discussion: {question}
        
        Final Round Transcript:
        {history}
        
        Your task:
        - Summarize only the decision, direction, or action that was **agreed upon** or **implicitly leaned toward**.
        - Avoid general summaries or listing all viewpoints.
        - If there's no clear agreement, say so.
        
        Respond with a clear, brief summary of the decision (1–2 sentences):"""