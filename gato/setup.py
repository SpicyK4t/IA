from distutils.core import setup
import py2exe

setup(name = "Gato IA",
	version="1.0",
	description="Gato bobo que se vuelve inteligente",
	author="Guillermo Villagomez",
	author_email="guillermoarturovillagomez@gmail.com",
	url="none",
	license="GPL",
	scripts=["gato_IA.py"],
	console=["gato_IA.py"]
)