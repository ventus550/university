import db
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from dateutil import parser

class DataWindow:

	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file("window.glade")
		builder.connect_signals(self)

		self.data = builder.get_object("Data")

		self.window = builder.get_object("DialogWindow")
		self.window.set_default_size(500,500)
		self.window.connect('destroy', Gtk.main_quit)


	def on_cell_edited(self, widget, path, text):
		if ':' not in str(path): return
		
		node = int(path.split(':')[0])
		cls = self.data[node][0]
		id = self.data[node][1]
		type = self.data[path][0]

		value = text
		try:
			if type == "people":
				text = [int(x) for x in text.strip("[]").replace(",", " ").split()]
				value = [db.getId(db.Person, id) for id in text]

			elif type == "date":
				value = parser.parse(text)
				text = value
			
			elif type == "film":
				value = int(text)

		except:
			db.err("Unexpected format: " + text)
			return


		obj = db.getId(db.classify(cls), id)
		setattr(obj, type, value)
		db.log("MODIFY " + str(obj))
		db.push(obj)

		self.data[path][1] = str(text)
	

	def on_add_click(self, button):
		new_person = db.Person(name='undefined', film='undefined')
		db.push(new_person)
		self.addEntry(new_person)
		db.log("PUSH " + str(new_person))
	

	def addEntry(self, ent):
		data = self.data
		row = None
		if isinstance(ent, db.Person):
			row = data.append(None, ["Person", str(ent.id)])
		else:
			row = data.append(None, ["Film", str(ent.id)])
			ent.people # force sync
		
		for var, value in vars(ent).items():
			if isinstance(value, list): value = [x.id for x in value]
			if var[0] != '_' and var != 'id': data.append(row, [str(var), str(value)])


	def show_all(self):
		self.window.show_all()



# Driver code
window = DataWindow()
for d in db.getAll():
	window.addEntry(d)
window.show_all()
Gtk.main()