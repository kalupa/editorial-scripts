#coding: utf-8
import workflow
import editor
import clipboard
import datetime

# entry_name = 'Journal 0{:%Y-%m-%d}'.format(datetime.date.today())
# filename = entry_name + '.markdown'

entry_file = workflow.get_variable('entry_filename')
daily_stats = workflow.get_variable('journal_stats')

file_contents = editor.get_file_contents(entry_file)

editor.set_file_contents(filename, file_contents + '\n\n' + daily_stats)

workflow.set_variable('entry_text', content)
workflow.set_variable('entry_filename', filename)

clipboard.set(content)
workflow.set_output(content)
