import re

def getPotencialDomains(lines):
    pattern = r"https?:\/\/(www\.|web\.|ww2\.)?([a-z0-9\-\.]+[a-z0-9\-]+)+(\/\w*)*"
    hostnames = []
    for i in lines:
        match_object = re.search(pattern, i)
        if match_object is not None:
             host_name = match_object.group(2)
             hostnames.append(host_name)
             print(host_name)
    return hostnames







arrayString = ["ut you http://www.lala.lala.com/kjbkb know, the beginners"," they’ll do what https://ww2.kazkas.la/kkaka beginners"," do. Andhttp://web.manosite.mano.com/kjllj/lhl eventually","they will http://hackerramk.com/1233 realize"," that the single responsibility principle is garbage. Well, maybe not directly.","Maybe they’ll be filled with a sense of Stockholm syndrome"]
print(getPotencialDomains(arrayString))
