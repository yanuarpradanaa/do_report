{
    "name" : "Delivery Order Prima Print", 
 	"category" : "Print out Delivery Order", 
    "version" : "1.0",
    "depends" : [
        'stock', #'report_py3o',
    ],
    "description": """
Print Out Delivery Order""",
    "author" : "Satusoft",
    "data" : [
        'report/do_pp.xml',
        'report/do_pp_document.xml',
        
    ],
    'installable' : True,
    'active' : False,
}