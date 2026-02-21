import os

def patch_file(filepath, replacements):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for old, new in replacements:
            content = content.replace(old, new)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched {filepath}")
    except Exception as e:
        print(f"Error patching {filepath}: {e}")

# index.html replacements
index_replacements = [
    ('class="fixed top-0 w-full z-50 transition-all duration-300 bg-transparent py-6"', 'class="fixed top-0 w-full z-50 transition-all duration-300 bg-white shadow-sm py-6"'),
    ('\\"className\\\":\\\"fixed top-0 w-full z-50 transition-all duration-300 bg-transparent py-6\\\"', '\\"className\\\":\\\"fixed top-0 w-full z-50 transition-all duration-300 bg-white shadow-sm py-6\\\"'),
    
    ('class="transition-all duration-300 brightness-0 invert"', 'class="transition-all duration-300"'),
    ('\\"className\\\":\\\"transition-all duration-300 brightness-0 invert\\\"', '\\"className\\\":\\\"transition-all duration-300\\\"'),
    
    ('class="font-medium transition hover:text-accent text-white"', 'class="font-medium transition hover:text-accent text-gray-700"'),
    ('\\"className\\\":\\\"font-medium transition hover:text-accent text-white\\\"', '\\"className\\\":\\\"font-medium transition hover:text-accent text-gray-700\\\"'),
    
    ('class="inline-block" href="/"><img alt="Akemis" loading="lazy" width="450" height="55" decoding="async" data-nimg="1" class="brightness-0 invert"', 'class="inline-block bg-white p-4 rounded-xl" href="/"><img alt="Akemis" loading="lazy" width="450" height="55" decoding="async" data-nimg="1" class=""'),
    ('\\"href\\\":\\\"/\\\",\\\"className\\\":\\\"inline-block\\\",\\\"children\\\":[\\\"$\\\",\\\"$L6\\\",null,{\\\"src\\\":\\\"/logo.png\\\",\\\"alt\\\":\\\"Akemis\\\",\\\"width\\\":450,\\\"height\\\":55,\\\"className\\\":\\\"brightness-0 invert\\\"}]}', '\\"href\\\":\\\"/\\\",\\\"className\\\":\\\"inline-block bg-white p-4 rounded-xl\\\",\\\"children\\\":[\\\"$\\\",\\\"$L6\\\",null,{\\\"src\\\":\\\"/logo.png\\\",\\\"alt\\\":\\\"Akemis\\\",\\\"width\\\":450,\\\"height\\\":55,\\\"className\\\":\\\"\\\"}]}')
]

patch_file('index.html', index_replacements)

# chunk replacement
chunk_replacements = [
    ('${e?"bg-white shadow-md py-4":"bg-transparent py-6"}', '${e?"bg-white shadow-md py-4":"bg-white shadow-sm py-6"}'),
    ('${!e?"brightness-0 invert":""}', '${!e?"":""}'),
    ('${e?"text-gray-700":"text-white"}', '${e?"text-gray-700":"text-gray-700"}')
]

js_dir = '_next/static/chunks'
for f in os.listdir(js_dir):
    if f.endswith('.js'):
        patch_file(os.path.join(js_dir, f), chunk_replacements)
