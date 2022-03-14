from cmd import Cmd
from index import app, db
from model import Querycollection
import xml.etree.ElementTree as ET


class MyCmd(Cmd):

    prompt = "> "

    def do_readxml(self, args):
        xmlfile = args
        tree = ET.parse(xmlfile)
        root = tree.getroot()
        for item in root.findall('./query'):
            question = item.find('question').text
            answer = item.find('answer').text
            data = Querycollection(question=question.strip(),
                                   answer=answer.strip())
            try:
                data.save()
            except db.NotUniqueError:
                print(question + " already exists")
            except Exception as e:
                print(str(e))
                return
        print("Inserted to database")

    def do_readcmd(self, args):
        question, answer = args.rsplit(":", 1)
        data = Querycollection(question=question.strip(),
                               answer=answer.strip())
        try:
            data.save()
        except Exception as e:
            print(str(e))
            return
        print("Inserted to database")

    def do_ask(self, args):
        question = args
        try:
            data = Querycollection.objects.get(question=question.strip())
        except Exception as e:
            print(str(e))
            return
        print(data["answer"])

    def do_del(self, args):
        question = args
        try:
            data = Querycollection.objects.get(question=question.strip())
            data.delete()
        except Exception as e:
            print(str(e))
            return
        print("Deleted from database")

    def do_display(self, args):
        try:
            data = Querycollection.objects.all_fields()
        except Exception as e:
            print(str(e))
            return
        for d in data:
            print("Question: " + d['question'] + "\nAnswer: " + d['answer'])

    def do_exit(self, args):
        raise SystemExit()


if __name__ == "__main__":
    app = MyCmd()
    app.cmdloop(
        'Enter a command to do something.\n Commands: readxml "xml file location", readcmd "question : answer", ask "question", del "question", display, exit')
