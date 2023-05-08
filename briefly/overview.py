import openai

api_key = "31f7f82f-294b-4f57-bee4-95740c738557"
openai.api_key = "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"

prefix = """
We are consultants helping to improve the communication between companies and marketing agencies by critiquing the marketing briefs that they give eachother.

Here is the overview section of a marketing brief produced by a company, that is then given to marketing agencies:
"""


def overview_is_concise(overview):
    
    message = f"""
{prefix}

{overview}

As well as providing all-important context, a brief overview is an opportunity to clearly define what you want from this campaign. It should be short, concise and in one or two sentences.

Is this overview clear and concise, in just one or two sentences and without using too jargon/buzzwords? (yes/no):
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    completion = response.choices[0].message['content']
    
    if 'yes' in completion.lower():
        return (True, "")
    elif "no" in completion.lower():
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=[
                {"role": "user", "content": message},
                {"role": "assistant", "content": "No."},
                {"role": "user", "content": "Make this brief clear, concise and just one or two short sentences. Use the format of 'To get to X [Objective] we need to engage Y [Target audience] and communicate Z [Key message + RTB]'"}
            ]
        )
        completion = response.choices[0].message['content']
        return (False, completion)
    else:
        raise RuntimeError("Response not yes/no")

    
# @st.cache_data(show_spinner="Checking whether overview is clear...")
def overview_is_inspiring(overview):
    message = f"""
{prefix}

{overview}

As well as providing all-important context, a brief overview is an opportunity to excite the marketing agency employees who are about to work on your project. 
Is should include a sentence about the thing that you find most exciting about this brief. 
It might be the fact that you’re launching a new product, or that certain market factors put you in a uniquely advantageous position.
Does this overview section do this, or is it a bit mundane and generic? (yes/no):
"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    completion = response.choices[0].message['content']
    
    if "yes" in completion.lower():
        return (True, "")
    elif "no" in completion.lower():
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=[
                {"role": "user", "content": message},
                {"role": "assistant", "content": "No."},
                {"role": "user", "content": "Suggest an alteration that is specifc and exciting."}
            ]
        )
        completion = response.choices[0].message['content']
        return (False, completion)
    else:
        raise RuntimeError()
    
overview_feedback_functions = [overview_is_concise, overview_is_inspiring]

overview_examples = [
    "The V&A is about to open a new exhibition called ‘Fashioning Masculinities’. This exhibition is the V&A’s first to focus on menswear, and celebrates the power, artistry and diversity of masculine attire and appearance. Juxtaposing contemporary and historic examples of fashion, sculpture, painting, drawing and photography from across the V&A collections and through key loans, it undresses, addresses and redresses masculinity from Renaissance Europe to the present day.",
    "This campaign is designed to drive sales of Peanuts Magazine by engaging school children and communicating that Peanuts is cool"
]