# Tests icons are being picked up properly by the often problematic GTK
# lookup mechanism. For a sample output checkout the link below:
# github.com/numixproject/numix-icon-theme/pull/777#issuecomment-148097809

from gi.repository import Gtk, Gdk, GdkPixbuf, Gio

class HelloWorldApp(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="apps.test.helloworld",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.connect("activate", self.on_activate)

    def on_activate(self, data=None):
        window = Gtk.Window(type=Gtk.WindowType.TOPLEVEL)
        window.set_title("Gtk3 Python Example")
        window.set_border_width(24)
        sizes = [16,22,24,32,48,64,96,128,256]
        vbox = Gtk.HBox()
        for size in sizes:
            fixed = Gtk.Fixed()
            image = Gtk.Image()
            icon_theme = Gtk.IconTheme.get_default()
            name = 'gtk-edit'
            pixbuf = icon_theme.load_icon(name, size, Gtk.IconLookupFlags.USE_BUILTIN)
            print(icon_theme.lookup_icon(name, size, 0).get_filename())
            image.set_from_pixbuf(pixbuf)
            vbox.pack_start(image, True, True, 10)
        window.add(vbox)
        window.show_all()
        self.add_window(window)

if __name__ == "__main__":
    app = HelloWorldApp()
    app.run(None)
