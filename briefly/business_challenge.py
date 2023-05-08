import openai
import os

openai.api_key = os.environ['openai_api_key']

prefix = """
We are consultants helping to improve the communication between companies and marketing agencies by critiquing the marketing briefs that they give eachother.

Here is the business challenge section of a marketing brief produced by a company, that is then given to marketing agencies:
"""

suffix = """
A great business challenge
- Is direct and concise
- Defines the nature of the problem: how you got here, and where you want to get to
- Diagnoses the problem without guessing at solutions
"""


def business_challenge_is_single_minded(business_challenge):
    message = f"""
{prefix}

{business_challenge}

{suffix}

Context on adjacent problems can be helpful, but be specific about the main problem this campaign needs to solve. If you aim to solve too many problems, you’ll likely end up solving none.

Does the business challenge above focus on the one key problem you this campaign to solve? or does it focus on more than one or two things? (yes/no)
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
                {"role": "assistant", "content": "Yes."},
                {"role": "user", "content": "Make this a great business challenges section by focusing on the one key problem this campaign to solve. Start with where your business currently is (and what challenge you might be facing), then explain what needs to change to improve things. Answer in two or three short concise sentences."}
            ]
        )
        completion = response.choices[0].message['content']
        return (False, completion)
    else:
        raise RuntimeError("Response not yes/no")
    
    
def business_challenge_is_jargon_free(business_challenge):
    message = f"""
{prefix}

{business_challenge}

{suffix}

Jargon can get in the way of someone understanding you. It might also contain a different meaning outside of your organisation than it does within it.

Is this business challenge section jargon free? (yes/no):
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
                {"role": "assistant", "content": "Yes."},
                {"role": "user", "content": "Make this a great business challenges section by using simpler language and avoiding jargon:"}
            ]
        )
        completion = response.choices[0].message['content']
        return (False, completion)
    else:
        raise RuntimeError("Response not yes/no")
    
    
def business_challenge_is_strategic(business_challenge):
    message = f"""
{prefix}

{business_challenge}

{suffix}

Jargon can get in the way of someone understanding you. It might also contain a different meaning outside of your organisation than it does within it.

In general, there are 5 strategic options for any comms activity:
1. Reach - Get more people to buy from you
2. Frequency - Get people to buy from you more often
3. Upsell - Get people to buy a more expensive version
4. Start - Get more people to start doing something
5. Stop - Get more people to stop doing something

Does this business challenge section fit into one of these options? (yes/no)
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
                {"role": "assistant", "content": "Yes."},
                {"role": "user", "content": "Make this a great business challenges section by being clearer about the change you need to see to solve your problem. Select the best fitting of the 5 srategic goals above and rewrite the business challenge into two or three sentences to describe it."}
            ]
        )
        completion = response.choices[0].message['content']
        return (False, completion)
    else:
        raise RuntimeError("Response not yes/no")
    
    
business_challenge_feedback_functions = [business_challenge_is_single_minded, business_challenge_is_jargon_free, business_challenge_is_strategic]

business_challenge_examples = [
    "Our sales are down and we need to sell more products.",
    "Food quality perceptions of Tesco's own branded food were low and lagging the category. They couldn’t make the same provenance claims other supermarkets were using, so they used the emotional connection we have with mealtimes to increase food quality perceptions by 41%. ",
    "Food quality perceptions of Tesco's own branded food were low and lagging the category. They couldn’t make the same provenance claims other supermarkets were using, so they used the emotional connection we have with mealtimes to increase food quality perceptions by 41%. We are also facing extreme competiion. We are also struggling to sell fast food and frozen food."
]