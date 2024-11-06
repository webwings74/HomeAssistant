# Tot nu toe heb ik geen werkende scripts kunnen maken met Python onder
# HomeAssistant. Het blijft een enigma.

# `data` is available as builtin and is a dictionary with the input data.
name = data.get("name", "world")

# `logger` and `time` are available as builtin without the need of explicit import.
logger.info("Hello {} at {}".format(name, time.time()))