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
    content = eval(content)
    print(content)
    return content

def typeOfDoctor(symptoms):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "I am giving you the list of types of doctors, and based on my problem/symptoms, you have to tell me which type of doctor is best suited for me.",
            },
            {
                "role" : "user",
                "content" : """Cardiologist: heart diseases - coronary artery disease, arrhythmias, and heart failure
                            Dermatologist: conditions of skin, hair, and nails- acne, eczema, and skin cancer
                            Endocrinologist: problems of endocrine system- diabetes, thyroid disorders, and hormonal imbalances
                            Gastroenterologist: disorders of the digestive system- gastrointestinal bleeding, irritable bowel syndrome (IBS), and Crohn's disease
                            Neurologist: nervous system- Parkinson's disease, epilepsy, and multiple sclerosis
                            Oncologist: cancer- chemotherapy, radiation therapy, and surgery
                            Orthopedic - musculoskeletal conditions- fractures, arthritis, and torn ligaments
                            Pediatrician: infants, children, and adolescents- vaccinations, growth and development, childhood illnesses
                            Psychiatrist: mental health disorders, including depression, anxiety, bipolar disorder, and schizophrenia
                            Pulmonologist: respiratory system-asthma, chronic obstructive pulmonary disease (COPD), and pneumonia.
                            Rheumatologist: autoimmune and inflammatory disorders affecting the joints and soft tissues- rheumatoid arthritis, lupus, and fibromyalgia
                            Ophthalmologist: eyes - cataracts, glaucoma & macular degeneration 
                            Urologist: urinary tract and male reproductive system- kidney stones, urinary incontinence, and prostate-related problems
                            Obstetrician-Gynecologist : women's reproductive health- pregnancy, childbirth, and disorders of the female reproductive system (menstrual disorders, infertility, and ovarian cysts /PCOS)
                            Trichologist: scalp and hair health
                            Radiologist: diagnosis of diseases and injuries using medical imaging techniques- x rays, ct scans, MRI scans, ultrasound & nuclear medicine"""
            },
            {
                "role" : "user",
                "content" : f"Here are my symptoms: {symptoms}"
            },
            {
                "role" : "user",
                "content" : "Please tell me the type of doctor now"            
            },
            {
                "role" : "user",
                "content" : "only give me type of doctor nothing else"            
            }
        ],
        model="gpt-3.5-turbo",
    )
    
    doctortype = chat_completion.choices[0].message.content
    print(doctortype)
    return doctortype



def doctorConnect(symptoms, patientName, doctorName, current_date, dob):
    med = medications(symptoms)
    doctorType = typeOfDoctor(symptoms)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Can you generate a prescription for my sample project for cough and cold, and these are the medicines I am planning to take: {med}",
            },
            {
                "role" : "user",
                "content" : f"The name of my patient is {patientName} and the name of the doctor is {doctorName}, and the date for the issue of the prescription is {current_date}, and the DOB of the patient is {dob}"
            },
            {
                "role" : "user",
                "content" : "Please give the prescription in the format:"
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
    print(content)
    return content
    
doctorConnect("my pandi is having cough and cold","Pandi","Simran",current_date,"2024-04-10")
