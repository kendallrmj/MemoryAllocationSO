import matplotlib.pyplot as plt
import numpy as np

category_names = ['Process 0', 'Process 1', 'Process 2', 'Process 3', 'Empty']
memories = {
    'FIRST FIT': [],
    'BEST FIT': [],
    'WORST FIT': [],
    'BUDDY SYSTEM': [],
}

def draw(firstFit, bestFit, worstFit, buddySystem):
    loadMemories(firstFit, bestFit, worstFit, buddySystem)
    survey(memories, category_names)
    plt.show()

def loadMemories(firstFit, bestFit, worstFit, buddySystem):
    tempList = []
    for block in firstFit:
        tempList.append(block[2])
    memories['FIRST FIT'] = tempList

    tempList = []
    for block in bestFit:
        tempList.append(block[2])
    memories['BEST FIT'] = tempList

    tempList = []
    for block in worstFit:
        tempList.append(block[2])
    memories['WORST FIT'] = tempList

    tempList = []
    for block in buddySystem:
        tempList.append(block[2])
    memories['BUDDY SYSTEM'] = tempList

def survey(memories, category_names):
    labels = list(memories.keys())
    data = np.array(list(memories.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)
    ax.legend(ncol=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

    return fig, ax