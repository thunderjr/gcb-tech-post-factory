TEXT_STYLES_HEADER = '\033[95m'
TEXT_STYLES_OKBLUE = '\033[94m'
TEXT_STYLES_OKCYAN = '\033[96m'
TEXT_STYLES_OKGREEN = '\033[92m'
TEXT_STYLES_WARNING = '\033[93m'
TEXT_STYLES_FAIL = '\033[91m'
TEXT_STYLES_ENDC = '\033[0m'
TEXT_STYLES_BOLD = '\033[1m'
TEXT_STYLES_UNDERLINE = '\033[4m'

def apply_styles(text, *args):
  return f"{''.join(args)}{text}{TEXT_STYLES_ENDC * len(args)}"

def log_success(title, description = ""): 
  print(("%s 🚀\n\n%s" % (apply_styles(title, TEXT_STYLES_BOLD, TEXT_STYLES_HEADER), description)).strip())

def log_error(title, description = ""): 
  print(("%s ⚠️\n\n%s" % (apply_styles(title, TEXT_STYLES_BOLD, TEXT_STYLES_FAIL), description)).strip())
