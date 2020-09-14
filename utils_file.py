import os
import json
import yaml

# local_data = {
#     'lang_prefix':{'French':'fr_to_en/',
#         'German':'de_to_en/',
#         'Italian':'it_to_en/',
#         'Spanish':'es_to_en/',
#         'Turkish':'tr_to_en/'},
#     'lang_options':[{"Label": "Deutsch", "Value": "German", "Selected": False},
#         {"Label": "Français", "Value": "French", "Selected": True},
#         {"Label": "Italiano", "Value": "Italian", "Selected": False},
#         {"Label": "Türk", "Value": "Turkish", "Selected": False},
#         {"Label": "Español", "Value": "Spanish", "Selected": False}],
#     'bleus':{"French" : "1-grams: 0.6588\nbi-grams: 0.5447\ntri-grams: 0.4940\n4-grams: 0.3815\n\nloss: 0.2570\nacc: 0.9801\nval_loss: 2.1694\nval_acc: 0.7039",
#         "German" : "1-grams: 0.6703\nbi-grams: 0.5568\ntri-grams: 0.5047\n4-grams: 0.3897\n\nloss: 0.2378\nacc: 0.9813\nval_loss: 2.1694\nval_acc: 0.7024",
#         "Italian" : "1-grams: 0.7932\nbi-grams: 0.7146\ntri-grams: 0.6588\n4-grams: 0.4915\n\nloss: 0.1287\nacc: 0.9840\nval_loss: 1.0991\nval_acc: 0.8213",
#         "Spanish" : "1-grams: 0.6442\nbi-grams: 0.5233\ntri-grams: 0.4715\n4-grams: 0.3637\n\nloss: 0.2208\nacc: 0.9840\nval_loss: 2.2772\nval_acc: 0.7074",
#         "Turkish" : "1-grams: 0.6796\nbi-grams: 0.5705\ntri-grams: 0.5154\n4-grams: 0.3732\n\nloss: 0.2303\nacc: 0.9767\nval_loss: 2.1991\nval_acc: 0.6970"},
#     'lang_details' : {"German" : "German Vocabulary Size: 13,834\nGerman Max Sentence Length: 17\n\nEnglish Vocabulary Size: 7,910\nEnglish Max Sentence Length: 8",
#         "French" : "French Vocabulary Size: 15,378\nFrench Max Sentence Length: 14\n\nEnglish Vocabulary Size: 7,468<\nEnglish Max Sentence Length: 8",
#         "Italian" : "Italian Vocabulary Size: 11772\nItalian Max Sentence Length: 17\n\nEnglish Vocabulary Size: 5296\nEnglish Max Sentence Length: 7",
#         "Spanish" : "Spanish Vocabulary Size: 16,831\nSpanish Max Sentence Length: 14\n\nEnglish Vocabulary Size: 8,943<\nEnglish Max Sentence Length: 10",
#         "Turkish" : "Turkish Vocabulary Size: 23,521\nTurkish Max Sentence Length: 9\n\nEnglish Vocabulary Size: 8,183\nEnglish Max Sentence Length: 7"},
#     'lang_index' : 'French'}

class Configurations():
    def __init__(self, config_file):
        # data = local_data

        self.config_file = config_file
        with open(config_file) as json_file:
            data = json.load(json_file)

        self.configs = data['configs']
        self.lang_prefix = data['configs']['lang_prefix']
        self.lang_options = data['configs']['lang_options']
        self.bleus = data['configs']['bleus']
        self.lang_details = data['configs']['lang_details']
        self.lang_index = data['configs']['lang_index']


    def write_config(self):
        stream = open('json_config.yaml', 'w')
        yaml.dump(self.configs, stream)    # Write a YAML representation of data to 'document.yaml'.
        print(yaml.dump(self.configs) )     # Output the document to the screen.

        # with open(self.config_file, 'w') as outfile:
        #     data = {}
        #     data['configs'] = {'bleus': self.bleus,
        #         'lang_details':self.lang_details,
        #         'lang_index':self.lang_index,
        #         'lang_prefix':self.lang_prefix,
        #         'lang_options':self.lang_options}
        #     json.dump(data, outfile)

    def load_config(self):
        return configs



if __name__ == '__main__':
    Config = Configurations(config_file='config.json')
    stream = open('json_config.yaml', 'w')
    yaml.dump(Config, stream)    # Write a YAML representation of data to 'document.yaml'.
    print(yaml.dump(Config) ) 
    # Config.write_config()
    # print(Config.data)
