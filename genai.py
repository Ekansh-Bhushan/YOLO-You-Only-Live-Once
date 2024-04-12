import os
from openai import OpenAI
from dotenv import main
from datetime import date

main.load_dotenv()
mykey = os.getenv("OPENAI_API_KEY")

client = OpenAI(
    api_key=mykey,
)

# Get the current date
current_date = date.today()


def medications(symptoms):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "I will ask you questions about\
                            which medication I should take to get\
                            recover from my problems. I will given \
                            you my medical symptoms and based on it \
                            first identify my medical problem\
                            and then return me a list of medicines\
                            i should take and please tell me the spicific medicines. You need to return the answer\
                            in the form of python list. say tell me your problem\
                            if you are ready",
            },
            {
                "role" : "user",
                "content" : f"here is my symptoms :{symptoms}"
            },
            {
                "role" : "user",
                "content" : "give me the names of the medication in proper python list and don't write anything else except the python list"
            }
        ],
        model="gpt-3.5-turbo",
    )

    content = chat_completion.choices[0].message.content
    content_list = eval(content)
    print(content_list)
    return content_list


def doctorConnect(symptoms,patientName,doctorName,current_date,dob):
    med = medications(symptoms)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"can you generate a prescription for \
                    my sample project for cough and cold and these are\
                          medicines i am planing to take {med}",
            },
            {
                "role" : "user",
                "content" : f"The name of my patient is {patientName}  and name of the doctor is {doctorName}\
                    and date for the issue of the prescription is {current_date} and DOB of the patient is {dob}"
            },
            {
                "role" : "user",
                "content" : "please give the prescription in the formate."
            },
            {
                "role" : "user",
                "content" : """Prescription:

                            Patient Name: [Your Name]
                            Issue Date: [Current Date]
                            Patient's Age : [Age]

                            Medications:
                            1. Cough Syrup - Take 10ml every 4-6 hours as needed for cough relief.
                            Sample Medication: Delsym, Robitussin, Mucinex
                            2. Decongestant - Take 1 tablet every 4-6 hours as needed for nasal congestion.
                            Sample Medication: Sudafed, Afrin, Claritin-D
                            3. Antihistamine - Take 1 tablet daily for allergy symptoms.
                            Sample Medication: Benadryl, Zyrtec, Allegra

                            Instructions:
                            - Continue with medications for 3-5 days.
                            - Avoid driving or operating machinery while taking medications.
                            - If symptoms worsen or persist after 3 days, consult a healthcare provider.

                            Doctor Signature: [Doctor's Name and Signature]
                            This prescription is valid for a period of 14 days."""
            },
            {
                "role" : "user",
                "content" : "Write the proper prescription and please write some sample names for these medicines also "
            },
        ],
        model="gpt-3.5-turbo",
    )

    content = chat_completion.choices[0].message.content
    # content_list = eval(content)
    print(content)
    return content
    

doctorConnect("my pandi is having cough and cold","Pandi","Simran",current_date,"2024-04-10")