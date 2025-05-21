import os, sys, getopt, subprocess, json

def normalize_language(language):
    if language == "golang" or language == "go":
        return "golang"
    return language

def transpile(file, language, source_language):
    language = normalize_language(language.lower())
    if language not in ["golang", "javascript", "typescript", "java", "kotlin", "python"]:
        raise ValueError("Unsupported language: {}".format(language))

    ai_guide = "Use CLAUDE.md as general guide for your response."
    ai_input = "{} Translate the {} code at {} to {} code.".format(
        ai_guide, source_language, file, language)
    args = [
        "claude", "-p", 
        ai_input,
    ]
    output = subprocess.check_output(args)

    if output[:5].lower() == b'error':
        print(output)
        raise Exception(output)
        return

    extension_map = {
        "golang": "go",
        "python": "py",
        "javascript": "js",
        "typescript": "ts",
        "java": "java",
        "kotlin": "kt",
    }
    extension = extension_map[language]

    last_dot = file.rfind(".")
    output_file = ".gen/{}/{}.{}".format(language, file[:last_dot], extension)

    # make output_file directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as f:
        f.write(output.decode("utf-8"))

    print(output)

def main(argv):
    options = ["file=", "lang=", "source_lang="]
    try:
      opts, args = getopt.getopt(argv,"f:l:s:",options)
    except getopt.GetoptError:
      print('options error')
      sys.exit(2)

    print("opts: {}".format(opts))
    print("args: {}".format(args))

    file = None
    language = None
    source_language = "Python"
    for opt, arg in opts:
      print ("opt: {}, arg: {}".format(opt, arg))
      if opt in ("-l", "--lang"):
         language = arg
      elif opt in ("-f", "--file"):
         file = arg
      elif opt in ("-s", "--source_lang"):
         source_language = arg

    transpile(file, language, source_language)

if __name__ == "__main__":
   main(sys.argv[1:])