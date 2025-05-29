import os, sys, getopt, subprocess, json, re

def normalize_language(language):
    if language == "golang" or language == "go":
        return "golang"
    return language

def get_language_extension(language):
    language = normalize_language(language.lower())
    extension_map = {
        "golang": "go",
        "python": "py",
        "javascript": "js",
        "typescript": "ts",
        "java": "java",
        "kotlin": "kt",
    }
    extension = extension_map[language]
    return extension

def transpile(file, language, source_language):
    language = normalize_language(language.lower())
    if language not in ["golang", "javascript", "typescript", "java", "kotlin", "python"]:
        raise ValueError("Unsupported language: {}".format(language))

    extension = get_language_extension(language)

    last_dot = file.rfind(".")
    output_file = ".gen/{}/{}.{}".format(language, file[:last_dot], extension)
    # make output_file directory if it doesn't exist
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    ai_guide = "Use CLAUDE.md as general guide for your response. "
    output_hint = "Contents will be written to {} by another program. Assume directory exists and import files from that directory if necessary.".format(output_file)
    ai_input = "{} Translate the {} code at {} to {} code. {}".format(
        ai_guide, source_language, file, language, output_hint)
    args = [
        "claude", "-p",
        ai_input,
    ]
    output = subprocess.check_output(args)

    if output[:5].lower() == b'error':
        print(output)
        raise Exception(output)
        return

    with open(output_file, "w") as f:
        code = extract_code(output.decode("utf-8"))
        f.write(code)

    # print(output)


def test_extract_code(source, language):
    extension = get_language_extension(language)
    last_dot = source.rfind(".")
    output_file = ".gen/{}/{}.{}".format(language, source[:last_dot], extension)
    input = ""
    print("output_file: {}".format(output_file))
    with open(output_file, "r") as f:
        input = f.read()
    with open(output_file, "w") as f:
        code = extract_code(input)
        f.write(code)


def extract_code(output):
    # Return everything between GENERATION START and # GENERATION END

    m = re.search('((?s:.)*?)GENERATION START(.*)?\n((?s:.)*?)\n.*GENERATION END', output)
    if m is None: 
        print("No explanation found in output")
        error = extract_error(output)
        if error is not None:
            raise Exception(error)
        return output

    print("Other output: ")
    CODE_GROUP_INDEX = 3
    code = m.group(CODE_GROUP_INDEX)
    for i, group in enumerate(m.groups()):
        # group method is 1-indexed but groups is 0-indexed
        if i == (CODE_GROUP_INDEX-1):
            continue
        print("group {}: {}".format(i, group))
    return code


def extract_error(output):
    # Given an agent output in the form of 
    # Explanation```language?code```more explanation
    # Return the code using regex
    m = re.search('##ERROR##: (.*, .*, .*)', output)
    if m is None:
        return None
    return m.group(1)

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
    # test_extract_code(file, language)

if __name__ == "__main__":
   main(sys.argv[1:])