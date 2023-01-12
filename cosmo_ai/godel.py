from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")
model = AutoModelForSeq2SeqLM.from_pretrained(
    "microsoft/GODEL-v1_1-large-seq2seq")



def generate(instruction, knowledge, dialog):
    FileLog = open("cosmo_ai/Data/godellog.txt", "r")
    chat_log = FileLog.read()
    FileLog.close()


    if knowledge != '':
        knowledge = '[KNOWLEDGE] ' + knowledge
    # dialog = ' EOS '.join(dialog)
    query = f"{instruction} [CONTEXT] {dialog} {knowledge}"
    input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=128,
                             min_length=8, top_p=0.9, do_sample=True)
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    chat_log_template_update = chat_log + \
        f"\nYou : {dialog} \nCosmo : {output}"
    FileLog = open("cosmo_ai/Data/godellog.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return output


# Instruction for a chitchat task
instruction = f'Instruction: given a dialog context and related knowledge, you need to empathically answer the question based on the knowledge.'

# Knowledge for a chitchat task
# know = open("cosmoai/cosmo_ai/Data/knowledge.txt", "r")
# knowledge = know.read()
knowledge = ''

# '''I am Cosmo. I help people be focused, goal oriented and productivity in life, I create reminders, tasks, todos, routines and schedule time. I motivate and inspires people to achieve their goals and follow routines with high discipline and dedication, and stay committed to their goal.
# I respond in happy, joyful, excited, positive, helpful, caring, passionate, friendly, enthusiastic, kind, generous, humble, wise way.'''
# Leave the knowldge empty

# while True:
#     dialog = input("You : ")
#     dialog = dialog.split(" EOS ")
#     response = generate(instruction, knowledge, dialog)
#     print(f'Cosmo : {response}')
