#coding: utf-8
import workflow

def process_stat(val0):
    val = float(val0)
    return '{:03.1f}'.format(lambda: val * 10 if val < 1 else val)

process_stats = lambda stats: map(process_stat, stats)

def get_stats(raw):
    print('raw: '+raw)
    stats = map(float, raw.split())
    #stats[3] = stats[3] * 10 # anxiety
    #stats[4] = stats[4] * 10 # energy
    #stats[5] = stats[5] * 10 # happiness
    #stats[7] = stats[7] * 10 # sleepqual
    return map(lambda n: '{:03.1f}'.format(n), stats)

#  Formats as GFM table
# | Header1         | Header2 |
# |-----------------|--------:|
# | Title1          |     0.0 |
# | Title2          |     0.0 |
def create_md_table (headers, titles, stats):
    line_template = '| {:<14} | {:>5} |\n'
    header_line = line_template.format(*headers)
    entry_lines = map(lambda t: line_template.format(*t), zip(titles, stats))
    table_break = '|{0:-<16}|{0:->6}:|\n'.format('')
    return header_line + table_break + ''.join(entry_lines)

headers = ('Daily Stats', '')
titles = [
        'Medication',
        'Alcohol',
        'Caffeine',
        'Anxiety',
        'Energy',
        'Happiness',
        'Sleep Hours',
        'Sleep Quality',
        'Systolic',
        'Diastolic'
        # 'Word Count',
]

stats = get_stats(workflow.get_input())
# print process_stats(workflow.get_input())
workflow.set_variable('journal_entry_stats',create_md_table(headers, titles, stats))
workflow.set_variable('csv_entry', ", ".join(map(str,stats)))
###
