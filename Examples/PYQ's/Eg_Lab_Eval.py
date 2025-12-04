def generate_purchase_report(data_string):

    raw_entries = data_string.strip().lstrip("[").rstrip("]").split("},")
    
    entries = []
    for raw in raw_entries:
        raw = raw.strip().lstrip("{").rstrip("},").rstrip("}")
        parts = raw.split(",")
        entry = {}
        for part in parts:
            key, value = part.split(":")
            key = key.strip().strip("'").strip('"')
            value = value.strip()
            if key == "name":
                entry[key] = value.strip("'").strip('"')
            else:
                entry[key] = int(value)
        entries.append(entry)
   
    

    from collections import defaultdict
    customer_book = defaultdict(lambda: defaultdict(list))
    category_book = defaultdict(list)
    

    for entry in entries:
        name = entry['name']
        for category in ['electronics', 'fashion', 'grocery']:
            if category in entry:
                amount = entry[category]
                customer_book[name][category].append(amount)
                category_book[category].append(amount)

    customer_summary = {}
    for name, categories in customer_book.items():
        amounts = []
        for cat_amounts in categories.values():
            amounts.extend(cat_amounts)
        total = sum(amounts)
        avg_per_category = total / len(categories)
        customer_summary[name] = amounts + [total, avg_per_category]
    

    category_summary = {}
    for category, amounts in category_book.items():
        total = sum(amounts)
        avg = total / len(amounts)
        category_summary[category.capitalize()] = amounts + [total, avg]
    
  
    prediction_category = max(category_summary.items(), key=lambda x: x[1][-1])[0]
    

    for name, summary in customer_summary.items():
        print(f"'{name}': {summary}")
    print()
    for category, summary in category_summary.items():
        print(f"'{category}': {summary}")
    print()
    print(f"Prediction: ‘{prediction_category}’ category is likely to generate the highest revenue.")
    

entries = '''
'name': 'Arun', 'electronics': 1200,
'name': 'Diya', 'fashion': 750,
'name': 'Arun', 'grocery': 300,
'name': 'Rahul', 'electronics': 2200,
'name': 'Diya', 'grocery': 450,
'name': 'Arun', 'fashion': 900
'''

generate_purchase_report(entries)


        