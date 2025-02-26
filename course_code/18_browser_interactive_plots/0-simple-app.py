import justpy as jp

def app():
    webPage = jp.QuasarPage()
    head1 = jp.QDiv(a = webPage, text = 'Analysis of Course Reviews', classes = 'text-h1 text-center q-pa-md')
    paragraph1 = jp.QDiv(a = webPage, text = 'These graphs represent course review analysis')
    
    return webPage

# Just add de fuction's name and juspy make the call.
jp.justpy(app)