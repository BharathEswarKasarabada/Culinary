import os
txt_files_exist = any(filename.endswith('.txt') for filename in os.listdir('runs/detect/predict/labels'))


def process_line(line, image_np):
    # Process a single line from the labels.txt file
    bresults = line.split()
    if len(bresults) >=10:
        names={
            0: 'avocado',
            1: 'beans',
            2: 'beet',
            3: 'bell pepper',
            4: 'broccoli',
            5: 'brus capusta',
            6: 'cabbage',
            7: 'carrot',
            8: 'cayliflower',
            9: 'celery',
            10: 'corn',
            11: 'cucumber',
            12: 'eggplant',
            13: 'fasol',
            14: 'garlic',
            15: 'hot pepper',
            16: 'onion',
            17: 'peas',
            18: 'potato',
            19: 'pumpkin',
            20: 'rediska',
            21: 'redka',
            22: 'salad',
            23: 'squash-patisson',
            24: 'tomato',
            25: 'vegetable marrow'
            }
        class_id = int(bresults[0])
        if class_id in names:
            label = names[class_id]
        else:
            label = 'Unknown'
    return label

if txt_files_exist:
    unique_labels=set()
    lis = open('runs/detect/predict/labels/image0.txt', 'r').readlines()
    for line in lis:
        
        