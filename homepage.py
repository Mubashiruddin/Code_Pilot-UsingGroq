import requests
import json
import streamlit as st

CURRENT_THEME = "light"
IS_DARK_THEME = False
EXPANDER_TEXT = ""

url="http://localhost:11434/api/generate"

headers={

    'Content-Type':'application/json'
}

history=[]

def generate_response(prompt,a):
    history.append(prompt)
    final_prompt="\n".join(history)
    if a==0:
        data={

            "model":"codepilot",
            "prompt":final_prompt,
            "stream":False
        }
    if a==1:
        data={

            "model":"codeoptimizer",
            "prompt":final_prompt,
            "stream":False
        }
    if a==2:
        data={

            "model":"chatbot",
            "prompt":final_prompt,
            "stream":False
        }
    if a==3:
        data={
            "model":"explainer",
            "prompt":final_prompt,
            "stream":False
        }

    response=requests.post(url,headers=headers,data=json.dumps(data))

    if response.status_code==200:
        response=response.text
        data=json.loads(response)
        actual_response=data['response']
        return actual_response
    else:
        print("error:",response.text)
    

def main():
    st.title("                    Code Pilot")
    st.markdown("<style>h1{color: white; font-size: 70px;}</style>", unsafe_allow_html=True)
    if st.button("💬Chatbot"):
        st.switch_page("pages/2_💬_chatbot.py")

    prompt = st.text_area("Enter your prompt", height=200)


    if st.button("Generate Code",key="button 1"):

        response = generate_response(prompt,0)
        st.write("Generated Code:")
        st.write(response)

    if  st.button("optimize code", key="button2"):
        response = generate_response(prompt,1)
        st.code(response)
    if st.button("explain Code",key="button 3"):
        response = generate_response(prompt,3)
        st.write("Explaination:")
        st.write(response)
if __name__ == "__main__":
    history = []  # Initialize history
    main()
    