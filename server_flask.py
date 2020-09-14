import os
from utils_file import CF
from flask import Flask, render_template, request
# from translator import Translator
# from keras.backend import clear_session
#


########################
### Step 1:  Declare session scope variables & methods
app = Flask(__name__)

def get_selected(options):
    for option in options:
        if option["Selected"]:
            return option["Value"]

def set_language(lang_index, lang_options):
    for option in lang_options:
        option["Selected"] = True if option["Value"] == lang_index else False

########################
### Step 2:  Build an Flask app to render each HTML page
###    @apps are the Flask object for HTML pages
###    Define an @app for each HTML page
###       1. '/' is the homepage
###       2. '/result' is the nearly identical page but with

### Step 2a: Render the home_screen
########
@app.route('/')
def home_screen():
    cf = CF(config_file='config.json')
    configs = cf.configs
    set_language(configs['lang_index'], configs['lang_options'])
    return render_template('index.html',
                            translation='',
                            options=configs['lang_options'],
                            selected_lang=get_selected(configs['lang_options']),
                            lang_details=configs['lang_details'][configs['lang_index']],
                            current_lang=configs['lang_index'],
                            bleu_score=configs['bleus'][configs['lang_index']])

### In this case, I wanted the results to appear as a separate page, and so I
###   created '/result', but it doesn't have to be a separate page.
###   I think I could just do everyting in the homepage ('/')
@app.route('/result',methods = ['POST', 'GET'])
def translate():
    if request.method == 'POST':

        # Get the results from the web user
        form_data = request.form
        for key, value in form_data.items():
            if key == 'Input_Text':
                input = value
                continue
            if key == 'Language':
                lang_index = value

        set_language(lang_index)

        # Get the model preferences locally or from S3
        s3_file = False

        try:
            if (s3_file):
                model_pref_path = 'machine-learning/models/' + lang_prefix[lang_index] + model_id + 'pickles/model_prefs.pkl'
                s3 = S3Bucket()
                #model_prefs = pickle.load(s3.read_pickle(model_pref_path))
                model_prefs = pickle.load(s3.load(model_pref_path))
            else:
                model_pref_path = 'models/' + lang_prefix[lang_index] + model_id + 'pickles/model_prefs.pkl'
                model_prefs = pickle.load(open(model_pref_path, 'rb'))

        except Exception as e:
            input = e
            translation_error = 'No Model found for {}'.format(model_pref_path)
            return render_template('index.html',
                                    input_echo=input,
                                    input_text='Unable to load language model: ' + lang_index,
                                    translation=translation_error,
                                    current_lang=lang_index,
                                    selected_lang=get_selected(lang_options),
                                    options=lang_options,
                                    lang_details=lang_details[lang_index],
                                    bleu_score=bleus[lang_index])

        # A model exists, so use it and translate away!
        T = Translator(model_prefs)
        translation = T.translate(input)
        #
        # # Keras backend needs to clear the session
        clear_session()
        return render_template('index.html',
                                input_echo=input,
                                input_text=input,
                                translation=translation,
                                selected_lang=get_selected(lang_options),
                                options=lang_options,
                                current_lang=lang_index,
                                lang_details=lang_details[lang_index],
                                bleu_score=bleus[lang_index])

        # for option in options:
        #     option["Selected"] = True if option["Value"] == lang_index else False
        # return render_template('index.html', input_text=input, translation=translation, selected_lang=get_selected(options), options=options)

if __name__ == '__main__':
    app.run(debug=True)
