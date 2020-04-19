from flask import request, render_template, Flask, jsonify, redirect, url_for
import numpy as np
import pandas as pd
import json
# Create the application.
APP = Flask(__name__)
value = []
global res
res = []

l1 = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity',
      'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety',
      'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough',
      'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea',
      'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes',
      'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
      'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region',
      'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid',
      'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness',
      'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort',
      'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium',
      'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
      'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
      'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring',
      'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']


disease = ['amphotericin', 'You have an allergy.You dont need any antibotics to treat.', 'tetracycline', 'Chronic cholestasis have been caused due to overdoseage of chlorpromazine,ibuprofen and amiodarone.',
           'This is due to Drug reaction', 'amoxicillin,tetracycline,levofloxacin', 'Co-trimoxazole', 'Cephalexin,Clindamycin [ penicillin injection ]',
           'Sulfamethoxazole,trimethoprim', 'Clarithromycin [ Biaxcin]', 'over doseage of Clarithromycin,erythromycin', 'aspirin [ Paracetamol]', 'Acetaminophen',
           'Paralysis (brain hemorrhage) .Surgery is required', 'Co-amoxiclav', 'Co-trimoxazole or Mirincamycin  or Tigecycline', 'acyclovir or valacyclovir',
           'Aspirin could worse the fever.Treatment for the symptoms is appropriate', 'Ciprofloxacin or Arythromycin or Offloxacin',
           'No specific antibiotics, avoid alcohol consumption', 'No specific antibiotics, avoid alcohol consumption',
           'No specific antibiotics, avoid alcohol consumption', 'No specific antibiotics, avoid alcohol consumption',
           'No specific antibiotics, avoid alcohol consumption', 'No specific antibiotics, avoid alcohol consumption',
           'Pyrazinamide,Ethambutol,Rifampin,Isoniazid', 'No Antibiotics required', 'Ciprofloxaxin and Levofloxaxin or Tetracycline', 'Doxycycline',
           'Overdosage of clarithromycin or azythromycin have the risk of causing heart attack', 'Augmentin', 'Levothyroxine or Liothyronine',
           'Methimazole', 'Clarithromycin', 'Doxycycline', 'Doxycycline', 'dimenhydrinate', 'tetracycline,doxycycline',
           'trimethoprim/sulfamethoxazole or ciprofloxacin or  cephalexin or levofloxacin', 'penicillin or erythromycin', 'Amoxicillin/clavulanate or clindamycin']

l2 = []
for x in range(0, len(l1)):
    l2.append(0)

# TESTING DATA df -------------------------------------------------------------------------------------
df = pd.read_csv("Training.csv")

df.replace({'prognosis': {'amphotericin': 0, 'You have an allergy.You dont need any antibotics to treat.': 1, 'tetracycline': 2, 'Chronic cholestasis have been caused due to overdoseage of chlorpromazine,ibuprofen and amiodarone.': 3,
                          'This is due to Drug reaction': 4, 'amoxicillin,tetracycline,levofloxacin': 5, 'Co-trimoxazole': 6, 'Cephalexin,Clindamycin [ penicillin injection ]': 7,
                          'Sulfamethoxazole,trimethoprim': 8, 'Clarithromycin [ Biaxcin]': 9, 'over doseage of Clarithromycin,erythromycin': 10, 'aspirin [ Paracetamol]': 11, 'Acetaminophen': 12,
                          'Paralysis (brain hemorrhage) .Surgery is required': 13, 'Co-amoxiclav': 14, 'Co-trimoxazole or Mirincamycin  or Tigecycline': 15, 'acyclovir or valacyclovir': 16,
                          'Aspirin could worse the fever.Treatment for the symptoms is appropriate': 17, 'Ciprofloxacin or Arythromycin or Offloxacin': 18,
                          'No specific antibiotics, avoid alcohol consumption': 19, 'No specific antibiotics, avoid alcohol consumption': 20,
                          'No specific antibiotics, avoid alcohol consumption': 21, 'No specific antibiotics, avoid alcohol consumption': 22,
                          'No specific antibiotics, avoid alcohol consumption': 23, 'No specific antibiotics, avoid alcohol consumption': 24,
                          'Pyrazinamide,Ethambutol,Rifampin,Isoniazid': 25, 'No Antibiotics required': 26, 'Ciprofloxaxin and Levofloxaxin or Tetracycline': 27, 'Doxycycline': 28,
                          'Overdosage of clarithromycin or azythromycin have the risk of causing heart attack': 29, 'Augmentin': 30, 'Levothyroxine or Liothyronine': 31,
                          'Methimazole': 32, 'Clarithromycin': 33, 'Doxycycline': 34, 'Doxycycline': 35, 'dimenhydrinate': 36, 'tetracycline,doxycycline': 37,
                          'trimethoprim/sulfamethoxazole or ciprofloxacin or  cephalexin or levofloxacin': 38, 'penicillin or erythromycin': 39, 'Amoxicillin/clavulanate or clindamycin': 40}}, inplace=True)
# print(df.head())
# print(df)
X = df[l1]

y = df[["prognosis"]]
# print(df[0:4920])
np.ravel(y)
# print(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr = pd.read_csv("Testing.csv")
tr.replace({'prognosis': {'amphotericin': 0, 'You have an allergy.You dont need any antibotics to treat.': 1, 'tetracycline': 2, 'Chronic cholestasis have been caused due to overdoseage of chlorpromazine,ibuprofen and amiodarone.': 3,
                          'This is due to Drug reaction': 4, 'amoxicillin,tetracycline,levofloxacin': 5, 'Co-trimoxazole': 6, 'Cephalexin,Clindamycin [ penicillin injection ]': 7,
                          'Sulfamethoxazole,trimethoprim': 8, 'Clarithromycin [ Biaxcin]': 9, 'over doseage of Clarithromycin,erythromycin': 10, 'aspirin [ Paracetamol]': 11, 'Acetaminophen': 12,
                          'Paralysis (brain hemorrhage) .Surgery is required': 13, 'Co-amoxiclav': 14, 'Co-trimoxazole or Mirincamycin  or Tigecycline': 15, 'acyclovir or valacyclovir': 16,
                          'Aspirin could worse the fever.Treatment for the symptoms is appropriate': 17, 'Ciprofloxacin or Arythromycin or Offloxacin': 18,
                          'No specific antibiotics, avoid alcohol consumption': 19, 'No specific antibiotics, avoid alcohol consumption': 20,
                          'No specific antibiotics, avoid alcohol consumption': 21, 'No specific antibiotics, avoid alcohol consumption': 22,
                          'No specific antibiotics, avoid alcohol consumption': 23, 'No specific antibiotics, avoid alcohol consumption': 24,
                          'Pyrazinamide,Ethambutol,Rifampin,Isoniazid': 25, 'No Antibiotics required': 26, 'Ciprofloxaxin and Levofloxaxin or Tetracycline': 27, 'Doxycycline': 28,
                          'Overdosage of clarithromycin or azythromycin have the risk of causing heart attack': 29, 'Augmentin': 30, 'Levothyroxine or Liothyronine': 31,
                          'Methimazole': 32, 'Clarithromycin': 33, 'Doxycycline': 34, 'Doxycycline': 35, 'dimenhydrinate': 36, 'tetracycline,doxycycline': 37,
                          'trimethoprim/sulfamethoxazole or ciprofloxacin or  cephalexin or levofloxacin': 38, 'penicillin or erythromycin': 39, 'Amoxicillin/clavulanate or clindamycin': 40}}, inplace=True)

X_test = tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)
# ------------------------------------------------------------------------------------------------------


@APP.route('/')
def index():
    return render_template('index.html')


@APP.route('/symptoms_checker')
def symptoms_checker():
    return render_template('checker.html')


@APP.route('/process', methods=['GET', 'POST'])
def process():
    value = request.args.get('key')
    print(value)
    list1 = (json.loads(value))
    print(list1)
    print(type(list1))
    global res
    res = []
    for i in range(0, 10):
        res.append(randomforest(list1))

    res = list(set(res))
    res = [sub.replace('Paralysis (brain hemorrhage) .Surgery is required',
                       'Paralysis (brain hemorrhage) .consult your healthcare') for sub in res]
    rew = res
    print(res)
    print("ew")
    print(rew)
    print(request.url)
    #render_template("antibioticsDetails.html", result=res)
    return jsonify(res)  # render_template("bb.html", result=res)


def randomforest(psymptoms):
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    # print(clf4)
    clf4 = clf4.fit(X, np.ravel(y))
    #psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    print(psymptoms)
    for k in range(0, len(l1)):
        for z in psymptoms:
            if(z == l1[k]):
                l2[k] = 1
    # print(l2)
    inputtest = [l2]
    predict = clf4.predict(inputtest)

    predicted = predict[0]
    # print(predicted)
    h = 'no'
    for a in range(0, len(disease)):
        if(predicted == a):
            h = 'yes'
            v = a
            break

    if (h == 'yes'):
        return disease[v]
    else:
        return
     # list of result


@APP.route('/antibiotics')
def antibiotics():
    print("list")
    print(res)
    return render_template('antibioticsDetails.html', result=res)


@APP.route('/find/<val>')
def find(val):
    dis = ''
    if(val == "Amphotericin"):
        dis = "amphotericin.html"

    elif(val == "tetracycline"):
        dis = "Tetracycline.html"

    elif (val == 'Chronic cholestasis have been caused due to overdoseage of chlorpromazine,ibuprofen and amiodarone.'):
        dis = "chronic.html"
    elif (val == 'amoxicillin,tetracycline,levofloxacin'):
        dis = 'atl.html'
    elif (val == 'Co-trimoxazole'):
        dis = 'cotri.html'
    elif (val == 'Cephalexin,Clindamycin [ penicillin injection ]'):
        dis = 'cecl.html'

    elif(val == 'Sulfamethoxazole,trimethoprim'):
        dis = 'sulfam.html'

    elif (val == 'Clarithromycin [ Biaxcin]'):
        dis = 'Biaxin.html'

    elif(val == 'aspirin [ Paracetamol]'):
        dis = 'Aspirin.html'

    elif (val == 'Acetaminophen'):
        dis = 'acetam.html'

    elif (val == 'Co-amoxiclav'):
        dis = 'coamoxi.html'

    elif(val == 'Co-trimoxazole or Mirincamycin  or Tigecycline'):
        dis = 'cmt.html'

    elif (val == 'acyclovir or valacyclovir'):
        dis = 'acyc.html'

    elif (val == 'Aspirin could worse the fever.Treatment for the symptoms is appropriate'):
        dis = 'Aspirin.html'

    elif (val == 'Ciprofloxacin or Arythromycin or Offloxacin'):
        dis = 'cao.html'

    elif (val == 'Pyrazinamide,Ethambutol,Rifampin,Isoniazid'):
        dis = 'peri.html'

    elif (val == 'Ciprofloxaxin and Levofloxaxin or Tetracycline'):
        dis = "clt.html"

    elif (val == 'Doxycycline'):
        dis = 'doxycycline.html'

    elif (val == 'Overdosage of clarithromycin or azythromycin have the risk of causing heart attack'):
        dis = 'clar_azy.html'

    elif(val == 'Augmentin'):
        dis = 'augmentin.html'

    elif (val == 'Levothyroxine or Liothyronine'):
        dis = 'levolio.html'

    elif(val == 'Methimazole'):
        dis = 'methimazole.html'

    elif(val == 'Clarithromycin'):
        dis = 'clarithromycin.html'

    elif (val == 'dimenhydrinate'):
        dis = 'dimenhydrinate.html'

    elif (val == 'tetracycline,doxycycline'):
        dis = 'tetra_doxycycline.html'

    elif(val == 'trimethoprim/sulfamethoxazole or ciprofloxacin or  cephalexin or levofloxacin'):
        dis = 'tsccl.html'

    elif (val == 'penicillin or erythromycin'):
        dis = 'pe_erythromycin.html'

    elif(val == 'Amoxicillin/clavulanate or clindamycin'):
        dis = 'amo_cla_cli.html'

    elif(val == 'You have an allergy.You dont need any antibotics to treat.' or val == 'This is due to Drug reaction' or
         val == 'Paralysis (brain hemorrhage) .Surgery is required' or
         val == 'No specific antibiotics, avoid alcohol consumption' or val == 'No Antibiotics required' or val == 'Paralysis (brain hemorrhage) .consult your healthcare'

         or val == 'over doseage of Clarithromycin,erythromycin'):
        return render_template("bb.html")

    return render_template(dis)


if __name__ == '__main__':
    APP.debug = True
    APP.run(debug=True)
