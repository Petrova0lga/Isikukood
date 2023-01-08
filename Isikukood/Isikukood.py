from Oma_moodul import parse_isikukood

while True:
    ik = input("Isikukood: ")
    try:
        form_ik = parse_isikukood(ik)
        print(form_ik)
    except Exception as e:
        if e.args[0] != '':
            print("Andmetüüp on vale, On vaja numbreid sisestada")


