import re

files = ['cv-standalone.html', 'src/App.jsx']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    start_tag = '<div id="cv-printable-template"'
    
    if start_tag in content:
        start_idx = content.find(start_tag)
        
        # Find the end of the printable template by looking for the next major layout marker
        # In App.jsx it's `<div ref={mainRef}`
        # In cv-standalone.html it's `<button onClick={() => setShowModal(true)}` or `<nav`
        
        end_idx_app = content.find('<div ref={mainRef}', start_idx)
        end_idx_html = content.find('</nav>', start_idx)
        
        end_idx = -1
        if end_idx_app != -1 and end_idx_html != -1:
            end_idx = min(end_idx_app, end_idx_html)
        elif end_idx_app != -1:
            end_idx = end_idx_app
        elif end_idx_html != -1:
            end_idx = end_idx_html
            
        if end_idx != -1:
            template = content[start_idx:end_idx]
            
            # Left column adjustments
            template = template.replace("height: '260px'", "height: '200px'")
            template = template.replace("marginBottom: '20px'", "marginBottom: '10px'")
            template = template.replace("padding: '0 20px 20px 20px'", "padding: '0 15px 15px 15px'")
            template = template.replace("marginBottom: '30px'", "marginBottom: '10px'")
            template = template.replace("lineHeight: '2'", "lineHeight: '1.4'")
            template = template.replace("lineHeight: '1.8'", "lineHeight: '1.3'")
            template = template.replace("margin: '0 0 30px 0'", "margin: '0 0 10px 0'")
            template = template.replace("fontSize: '18px'", "fontSize: '14px'")
            
            # Right column adjustments
            template = template.replace("padding: '30px 30px 30px 20px'", "padding: '15px 15px 15px 10px'")
            template = template.replace("fontSize: '42px'", "fontSize: '28px'")
            template = template.replace("fontSize: '16px'", "fontSize: '12px'")
            template = template.replace("marginBottom: '25px'", "marginBottom: '10px'")
            template = template.replace("marginBottom: '15px'", "marginBottom: '6px'")
            template = template.replace("marginBottom: '10px'", "marginBottom: '4px'")
            template = template.replace("marginTop: '20px'", "marginTop: '10px'")
            template = template.replace("padding: '5px 10px'", "padding: '3px 6px'")
            template = template.replace("lineHeight: '1.6'", "lineHeight: '1.3'")
            template = template.replace("paddingLeft: '35px'", "paddingLeft: '15px'")
            template = template.replace("marginBottom: '3px'", "marginBottom: '1px'")
            template = template.replace("marginBottom: '5px'", "marginBottom: '2px'")
            template = template.replace("fontSize: '14px'", "fontSize: '12px'")
            template = template.replace("fontSize: '13px'", "fontSize: '11px'")
            
            new_content = content[:start_idx] + template + content[end_idx:]
            
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Replaced in {file}")
        else:
            print(f"Could not find end tag in {file}")
    else:
        print(f"Could not find start tag in {file}")
