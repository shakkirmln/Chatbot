from cmd import Cmd
from index import app
from model import Querycollection
from flask import jsonify


class MyCmd(Cmd):

    prompt = "> "

    def do_readxml(self, args):
        name, cost = args.rsplit(" ", 1)
        print('Created "{}", cost ${}'.format(name, cost))

    def do_readcmd(self, args):
        name, cost = args.rsplit(" ", 1)
        print('Created "{}", cost ${}'.format(name, cost))

    def do_ask(self, args):
        # name, cost = args.rsplit(" ", 1)
        question = args
        try:
            data = Querycollection.objects.get(question=question)
        except Exception as e:
            print(str(e))
            return
        print(data["answer"])

    def do_del(self, args):
        question = args
        try:
            data = Querycollection.objects.get(question=question)
            data.delete()
        except Exception as e:
            print(str(e))
            return
        print("Deleted")

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
        'Enter a command to do something.\n Commands: readxml, readcmd, ask, del, display, exit')
