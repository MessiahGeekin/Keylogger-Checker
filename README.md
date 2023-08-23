<h1>Keylogger Detection Script</h1>

<p>A Python script to detect potential keyloggers based on suspicious keywords in process names.</p>

<h2>Usage</h2>

<p>This script uses the <code>psutil</code> library to identify potential keyloggers based on a list of suspicious keywords from a JSON file.</p>
<ol>
    <li>Ensure you have Python and the <code>psutil</code> library installed.</li>
    <li>Create a JSON file named <code>keywords.json</code> with a list of suspicious keywords.</li>
    <li>Run the script using the following command:</li>
</ol>

<pre><code>python main.py</code></pre>

<h2>Script Structure</h2>

<p>The script consists of the following components:</p>
<ul>
    <li><strong><code>load_json_file()</code></strong>: Loads suspicious keywords from <code>keywords.json</code>.</li>
    <li><strong><code>checking(keywords)</code></strong>: Iterates through running processes and detects potential keyloggers based on keywords.</li>
    <li><strong><code>main()</code></strong>: The main function to execute the script.</li>
</ul>

<h2>Customization</h2>

<p>You can customize the <code>keywords.json</code> file with your own list of suspicious keywords.</p>
