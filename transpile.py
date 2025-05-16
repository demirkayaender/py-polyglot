import os, sys, getopt, subprocess, json

def transpile(file, language, output_file):
    language = language.lower()
    if language not in ["golang", "go", "javascript", "typescript", "java", "kotlin", "python"]:
        raise ValueError("Unsupported language: {}".format(language))

    ai_guide = "Use CLAUDE.md as general guide for your response."
    ai_input = "{} Translate the Python code at {} to {} code.".format(ai_guide, file, language)
    args = [
        "claude", "-p", 
        ai_input,
    ]
    output = subprocess.check_output(args)

    # make output_file directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as f:
        f.write(output.decode("utf-8"))

    print(output)

def main(argv):
    options = ["file=", "lang=", "output="]
    try:
      opts, args = getopt.getopt(argv,"f:l:o:",options)
    except getopt.GetoptError:
      print('options error')
      sys.exit(2)

    print("opts: {}".format(opts))
    print("args: {}".format(args))

    file = None
    language = None
    output = None
    for opt, arg in opts:
      print ("opt: {}, arg: {}".format(opt, arg))
      if opt in ("-l", "--lang"):
         language = arg
      elif opt in ("-f", "--file"):
         file = arg
      elif opt in ("-o", "--output"):
         output = arg

    transpile(file, language, output)

if __name__ == "__main__":
   main(sys.argv[1:])