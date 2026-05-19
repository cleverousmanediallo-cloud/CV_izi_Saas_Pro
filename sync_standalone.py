import re

# Read the contents
with open('src/App.jsx', 'r', encoding='utf-8') as f:
    app_jsx = f.read()

with open('cv-standalone.html', 'r', encoding='utf-8') as f:
    standalone_html = f.read()

# Extract the App component
match = re.search(r'export default function App\(\) \{(.*?)\Z', app_jsx, re.DOTALL)
if match:
    app_body = match.group(1)
    
    # In cv-standalone.html, find where `function App() {` starts and replace everything up to `const root = ReactDOM.createRoot`
    # We will also insert the lucide component wrappers before the App component
    
    lucide_components = """
        const Icon = ({ name, size = 24 }) => {
            return <i data-lucide={name} style={{ width: size, height: size, display: 'inline-block' }}></i>;
        };
        const Download = ({ size }) => <Icon name="download" size={size} />;
        const Mail = ({ size }) => <Icon name="mail" size={size} />;
        const Phone = ({ size }) => <Icon name="phone" size={size} />;
        const Linkedin = ({ size }) => <Icon name="linkedin" size={size} />;
        const ExternalLink = ({ size }) => <Icon name="external-link" size={size} />;
        
        function App() {""" + app_body
    
    # We need to make sure lucide.createIcons() is called after render.
    # In App.jsx, there is a useEffect with `gsap.context`.
    app_body_patched = app_body.replace("useEffect(() => {", "useEffect(() => {\n      if (window.lucide) { window.lucide.createIcons(); }", 1)
    
    # Map absolute paths back to relative paths for python server
    app_body_patched = app_body_patched.replace('"/Photos images/', '"public/Photos images/')
    
    lucide_components = """
        const Icon = ({ name, size = 24 }) => {
            return <i data-lucide={name} style={{ width: size, height: size, display: 'inline-block' }}></i>;
        };
        const Download = ({ size, className }) => <i data-lucide="download" className={className} style={{ width: size, height: size, display: 'inline-block' }}></i>;
        const Mail = ({ size, className }) => <i data-lucide="mail" className={className} style={{ width: size, height: size, display: 'inline-block' }}></i>;
        const Phone = ({ size, className }) => <i data-lucide="phone" className={className} style={{ width: size, height: size, display: 'inline-block' }}></i>;
        const Linkedin = ({ size, className }) => <i data-lucide="linkedin" className={className} style={{ width: size, height: size, display: 'inline-block' }}></i>;
        const ExternalLink = ({ size, className }) => <i data-lucide="external-link" className={className} style={{ width: size, height: size, display: 'inline-block' }}></i>;
        
        function App() {""" + app_body_patched
        
    pattern = re.compile(r'const Icon = \(\{ name, size = 24 \}\) => \{.*?function App\(\) \{.*?\}\s+(?=const root = ReactDOM\.createRoot)', re.DOTALL)
    
    new_standalone = pattern.sub(lucide_components, standalone_html)
    
    with open('cv-standalone.html', 'w', encoding='utf-8') as f:
        f.write(new_standalone)
        
    print("Standalone HTML updated successfully.")
else:
    print("Failed to find App in App.jsx")
