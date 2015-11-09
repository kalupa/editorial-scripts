#coding: utf-8
import workflow
import editor
import clipboard
import datetime

raw_entry = workflow.get_variable('entry_text')

entry_name = 'Journal 0{:%Y-%m-%d}'.format(datetime.date.today())
content = '# ' + entry_name + '\n\n' + raw_entry
content = content.strip() + '\n'
filename = entry_name + '.markdown'
# daily_stats = workflow.get_variable('journal_stats')

editor.set_file_contents(filename, content)
#editor.set_file_contents(filename, content + '\n\n' + daily_stats)

workflow.set_variable('entry_text', content)
workflow.set_variable('entry_filename', filename)

clipboard.set(content)
workflow.set_output(content)
