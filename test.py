data = {'%**_': ['Master Your Emotions _ Sedona Method ( PDFDrive ).pdf', 'Mathematics for Computer Science.pdf', 'My resume_220726_231216.pdf'], 'samples': {'%**_': ['12-Rules-for-Life.pdf', '14-05-2021-133654Dark-Psychology -James-Williams.pdf', '4-hour-body - Timothy Ferriss.pdf', 'Atomic Habits.pdf', 'Ben Carson  -You Have A Brain (Naijasermons.com.ng).pdf', 'Blink by Malcom Gladwell – The Power of Thinking Without Thinking ( PDFDrive ).pdf', 'BOOKS.YOSSR.COM-Noise-A-Flaw-in-Human-Judgment.pdf'], 'Examples': {'%**_': ['Booktree.ng_the-Law-of-Attraction.pdf', 'Charles Duhigg - The Power of Habit.pdf', 'descartes-error_antonio-damasio.pdf', 'dokumen.pub_machine-learning-for-algorithmic-trading-predictive-models-to-extract-signals-from-market-and-alternative-data-for-systematic-trading-strategies-with-python-2nd-edition-2nbsped-9781839216787-1839216786.epub', 'dokumen.pub_python-for-algorithmic-trading-from-idea-to-cloud-deployment-1nbsped-149205335x-9781492053354.epub'], 'colloquial': {'%**_': ['Duncan Clark - Alibaba_ The House That Jack Ma Built-Ecco Press (2016).pdf', 'Emotional Intelligence.pdf', 'Greatest_Salesman_in_the_World.pdf', 'Hall_Edward_T_Beyond_Culture.pdf', 'How to Talk to Anyone 92 Little Tricks for Big Success in Relationships by Leil Lowndes.pdf', 'Influence_ The Psychology of Persuasion ( PDFDrive ).pdf']}, 'epoistemology': {'%**_': ['Duncan Clark - Alibaba_ The House That Jack Ma Built-Ecco Press (2016).pdf', 'Emotional Intelligence.pdf', 'Greatest_Salesman_in_the_World.pdf', 'Hall_Edward_T_Beyond_Culture.pdf', 'How to Talk to Anyone 92 Little Tricks for Big Success in Relationships by Leil Lowndes.pdf', 'Influence_ The Psychology of Persuasion ( PDFDrive ).pdf']}}}}
#hksxkcj
res = []
def flatten(data):
    for ent in data.keys():
        if isinstance(data[ent], dict):
            flatten(data[ent])
        else:
            res.extend(data[ent])
            print(res)
    return res
print(flatten(data))