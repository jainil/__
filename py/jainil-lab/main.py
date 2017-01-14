import cgi
import datetime
import urllib
import webapp2
import jinja2
import os

#for email
from google.appengine.api import mail

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

from google.appengine.ext import db
from google.appengine.api import users


class Greeting(db.Model):
  """Models an individual Guestbook entry with an author, content, and date."""
  author = db.UserProperty()
  content = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)


def guestbook_key(guestbook_name=None):
  """Constructs a Datastore key for a Guestbook entity with guestbook_name."""
  return db.Key.from_path('Guestbook', guestbook_name or 'default_guestbook')


# class MainPage(webapp2.RequestHandler):
  # def get(self):
    # self.response.out.write('<html><body>')
    # guestbook_name=self.request.get('guestbook_name')

    # # Ancestor Queries, as shown here, are strongly consistent with the High
    # # Replication Datastore. Queries that span entity groups are eventually
    # # consistent. If we omitted the ancestor from this query there would be a
    # # slight chance that Greeting that had just been written would not show up
    # # in a query.
    # greetings = db.GqlQuery("SELECT * "
                            # "FROM Greeting "
                            # "WHERE ANCESTOR IS :1 "
                            # "ORDER BY date DESC LIMIT 10",
                            # guestbook_key(guestbook_name))

    # for greeting in greetings:
      # if greeting.author:
        # self.response.out.write(
            # '<b>%s</b> wrote:' % greeting.author.nickname())
      # else:
        # self.response.out.write('An anonymous person wrote:')
      # self.response.out.write('<blockquote>%s</blockquote>' %
                              # cgi.escape(greeting.content))

    # self.response.out.write("""
          # <form action="/sign?%s" method="post">
            # <div><textarea name="content" rows="3" cols="60"></textarea></div>
            # <div><input type="submit" value="Sign Guestbook"></div>
          # </form>
          # <hr>
          # <form>Guestbook name: <input value="%s" name="guestbook_name">
          # <input type="submit" value="switch"></form>
        # </body>
      # </html>""" % (urllib.urlencode({'guestbook_name': guestbook_name}),
                          # cgi.escape(guestbook_name)))

class MainPage(webapp2.RequestHandler):
    def get(self):
        guestbook_name=self.request.get('guestbook_name')
        greetings_query = Greeting.all().ancestor(
            guestbook_key(guestbook_name)).order('-date')
        greeting = greetings_query.fetch(10)

        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'greetings': greeting,
            'url': url,
            'url_linktext': url_linktext,
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))

class Guestbook(webapp2.RequestHandler):
  def post(self):
    # We set the same parent key on the 'Greeting' to ensure each greeting is in
    # the same entity group. Queries across the single entity group will be
    # consistent. However, the write rate to a single entity group should
    # be limited to ~1/second.
    guestbook_name = self.request.get('guestbook_name')
    greeting = Greeting(parent=guestbook_key(guestbook_name))

    if users.get_current_user():
      greeting.author = users.get_current_user()

    greeting.content = self.request.get('content')
    greeting.put()
    self.redirect('/?' + urllib.urlencode({'guestbook_name': guestbook_name}))

class Map(webapp2.RequestHandler):
  def get(self):
    randommap=jinja_environment.get_template('mydevour.htm')
    self.response.out.write(randommap.render())

class SendMail(webapp2.RequestHandler):
  def post(self):
    sender_address="jainil jainil.parekh@iitgn.ac.in"
    subject = "hi"
    body="hi"
    mail.send_mail(sender_address, '6265868616@tmomail.net', subject, body)

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/sign', Guestbook),
                               ('/map', Map),
                               ('/mail',SendMail)],
                              debug=True)