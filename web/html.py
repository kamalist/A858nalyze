
from cgi import escape

def _wrapper(name):
	def attr_str(item):
		key, value = item
		return " %s='%s'" % (key, escape(value, True))
	def attrs_str(attrs):
		return "".join(map(attr_str, attrs.items()))
	def result(*inner, **attrs):
		x = "".join(inner)
		return "<%s%s>%s</%s>" % (name, attrs_str(attrs), x, name)
	return result

def _list_wrapper(name):
	_tag_wrapper = _wrapper(name)
	def result(*items):
		items = map(lambda x: "<li> " + x, items)
		return _tag_wrapper(*items)
	return result

html = _wrapper('html')
body = _wrapper('body')
head = _wrapper('head')
title = _wrapper('title')

tt = _wrapper('tt')
pre = _wrapper('pre')

h1 = _wrapper('h1')
h2 = _wrapper('h2')
h3 = _wrapper('h3')

ul = _list_wrapper('ul')
ol = _list_wrapper('ol')

a = _wrapper('a')

