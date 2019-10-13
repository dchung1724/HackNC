import create_dict
import predict
import os
import yaml
import sys

def parse_dict(filename, map):
    # description: opens yaml config file and sets LABEL_MAP to parsed dictionary
    # input: filepath to the map file
    # output: none but global var LABEL_MAP will be set to parsed dictionary

    if os.path.exists(filename):
        with open(filename, 'r') as stream:
            try:
                map = yaml.load(stream, Loader=yaml.FullLoader)
            except yaml.YAMLError as exc:
                print(exc)
        return map
    else:
        print("Error: Label file: <" + filename + "> does not exist..\n")
        exit()



def main():
    image = os.environ['IMAGE_PATH']
    project_id = os.environ['PROJECT_ID']
    model_id = os.environ['MODEL_ID']
    try:
        image_label_details = predict.get_label(image, project_id, model_id)
        image_label = (image_label_details.payload[0].display_name)
        image_score = (image_label_details.payload[0].classification.score)

        create_dict.create_dictionary()
        county_dict = []
        county_dict = parse_dict('/Users/hyunc/Desktop/HackNC/result.yaml', county_dict)
        #print(county_dict)

        do_not_include_value = False
        include_value = False
        print("Found! The label for image is:", image_label)
        print("With an accuracy of:", image_score)
        for group_name, group_dict in county_dict.items():
            #print(group_name)
            #print(group_dict)
            if (do_not_include_value == False):
                for item in group_dict['Do not include']:
                    #print(item)
                    if image_label == item:
                        do_not_include_value = True
                        break
            if (include_value == False):
                for item in group_dict['Include']:
                    if image_label == item:
                        include_value = True
                        break
        #print(include_value, do_not_include_value)
        if ((include_value == True) & (do_not_include_value == False)):
            print("Yay! You can recycle!")
        else:
            print("Can't recycle! Try another item.")
    except:
        print("Sorry! Can't find the name of the object in the picture. Please try again!")


if __name__== "__main__":
    main()
