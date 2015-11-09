#coding: utf-8
import workflow
import editor
import clipboard
import datetime


entry_file = workflow.get_variable('entry_filename')
file_contents = editor.get_file_contents(entry_file)

if (file_contents):
    entry = file_contents
else:
    entry = 'empty'

daily_stats = workflow.get_variable('journal_stats')
print('daily_stats' + daily_stats)

editor.set_file_contents(filename, entry + '\n\n' + daily_stats)

workflow.set_variable('entry_text', content)
workflow.set_variable('entry_filename', filename)

clipboard.set(content)
workflow.set_output(content)
