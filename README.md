# SOAP Service Demo with JMeter Load Test

## Ce face?
- expune un serviciu SOAP pe http://localhost:8000
- endpoint-ul `say_hello(name)` răspunde cu `Hello, name!`

## Cum rulezi?
1. Instalează dependințele:
   ```
   pip install -r requirements.txt
   ```
2. Rulează serverul SOAP:
   ```
   python soap_server.py
   ```
3. Rulează un test rapid cu curl:
   ```
   curl -X POST http://localhost:8000 -H "Content-Type: text/xml" -d '
   <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:spy="spyne.examples.hello">
     <soapenv:Header/>
     <soapenv:Body>
        <spy:say_hello>
           <spy:name>Georgiana</spy:name>
        </spy:say_hello>
     </soapenv:Body>
   </soapenv:Envelope>'
   ```

## Tools
- Python, Spyne (SOAP)
- JMeter pentru load test (fișierul .jmx poate fi configurat separat)

## Autor
Georgiana M.
