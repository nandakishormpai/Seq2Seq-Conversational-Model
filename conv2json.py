import os
import pprint
import json

def movie_maker(main_dict):
    myfile = open(os.path.join("cornell_movie_dialogs_corpus","cornell movie-dialogs corpus","movie_titles_metadata.txt"), "r",errors="surrogateescape")
    try:
        for i,line in enumerate(myfile):
            line = line.split(" +++$+++ ")
            movie_name = line[1]
            movie_id = line[0]
            main_dict[line[0]]={}
            (main_dict[line[0]])["name"]=line[1]
            (main_dict[line[0]])["characters"]={}
            (main_dict[line[0]])["conversations"]=[]
    except:
        print(i)
    myfile.close()
    return main_dict

def character_maker(main_dict):
    myfile = open(os.path.join("cornell_movie_dialogs_corpus","cornell movie-dialogs corpus","movie_characters_metadata.txt"), "r",errors="surrogateescape")
    try:
        for i,line in enumerate(myfile):
            line = line.split(" +++$+++ ")
            char_name = line[1]
            char_id = line[0]
            movie_id = line[2]
            ((main_dict[movie_id])["characters"])[char_id] = { "name" : char_name, "lines" : {} }
            
    except:
        print(i)
    myfile.close()
    return main_dict

def line_maker(main_dict):
    myfile = open(os.path.join("cornell_movie_dialogs_corpus","cornell movie-dialogs corpus","movie_lines.txt"), "r",errors="surrogateescape")
    try:
        for i,line in enumerate(myfile):
            line = line.split(" +++$+++ ")
            line_id = line[0]
            char_id = line[1]
            movie_id = line[2]
            dialogue = (line[4]).replace("\n","")
            ((((main_dict[movie_id])["characters"])[char_id])["lines"])[line_id] = dialogue
    except:
        print(i)
    myfile.close()
    return main_dict

def conv_maker(main_dict):
    myfile = open(os.path.join("cornell_movie_dialogs_corpus","cornell movie-dialogs corpus","movie_conversations.txt"), "r",errors="surrogateescape")
    try:
        for i,line in enumerate(myfile):
            #print(i)
            line = line.split(" +++$+++ ")
            char1_id = line[0]
            char2_id = line[1]
            movie_id = line[2]
            line[3] = (line[3].replace("\n",""))[1:-1]
            line[3] = line[3].replace(" ","")
            convid_list = (line[3].replace("'","")).split(",")
            conv_list=[]
            for line_id in convid_list:
                try:
                    dialogue = ((((main_dict[movie_id])["characters"])[char1_id])["lines"])[line_id]
                except:
                    dialogue = ((((main_dict[movie_id])["characters"])[char2_id])["lines"])[line_id]
                conv_list.append(dialogue)
            ((main_dict[movie_id])["conversations"]).append(conv_list)
            '''
            line = line.split(" +++$+++ ")
            line_id = line[0]
            char_id = line[1]
            movie_id = line[2]
            dialogue = (line[4]).replace("\n","")
            ((((main_dict[movie_id])["characters"])[char_id])["lines"])[line_id] = dialogue
            '''
    except Exception as e:
        print(e)
    myfile.close()
    return main_dict



if __name__ == "__main__":
    main_dict = {}
    main_dict = movie_maker(main_dict)
    main_dict = character_maker(main_dict)
    main_dict = line_maker(main_dict)
    main_dict = conv_maker(main_dict)
    movies = open("data.json", "w")
    movies = json.dump(main_dict, movies)
    #pprint.pprint(main_dict)