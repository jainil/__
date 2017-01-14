x="""
<!DOCTYPE html>
<html>
  <head>
<!--[if lt IE 9]>
<script src="/static/html5.js"></script>
<![endif]-->
    <meta charset="utf-8" />
    <link rel="alternate" type="application/atom+xml"
          title="Programming Google App Engine" href="/blog/atom.xml" />
    <link href="http://fonts.googleapis.com/css?family=Candal" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Shanti" rel="stylesheet" type="text/css">
    <link href="http://fonts.googleapis.com/css?family=Inconsolata" rel="stylesheet" type="text/css">
    <link rel="stylesheet" type="text/css" href="/static/prettify/prettify.css" />
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
    <script src="/static/prettify/prettify.js"></script>
    <script>
      $(document).ready(function () { prettyPrint(); });
    </script>
    <link rel="stylesheet" type="text/css" href="/static/styles.css" />
    <title>Programming Google App Engine</title>
    

    <script type="text/javascript">
      var _gaq = _gaq || [];
      _gaq.push(['_setAccount', 'UA-11040426-2']);
      _gaq.push(['_trackPageview']);

      (function() {
        var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
        ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
        var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
      })();
    </script>
  </head>
  <body>
    <header class="outer">
      <div class="innerbox">
        <h1><a href="/">Programming Google App Engine</a></h1>
      </div>
      <nav class="innerbox primarynav">
        <ul>
          <li><a href="/">News &amp; Articles</a></li>
          <li><a href="/code">Code &amp; Extras</a></li>
          <li><a href="/about">About the Book</a></li>
          <li><a href="/contact">Contact the Author</a></li>
        </ul>
      </nav>
      
    </header>
    <div class="bodyouter outer">
      <div class="bodybox innerbox">

        <div class="mainbox">

          <article>
            <header>
              <h1><a href="/blog/entry/RC_update_in_flight__new_intro_tutorials__Blobstore_chapter">RC update in flight: new intro tutorials, Blobstore chapter</a></h1>
              <div class="pubdate"><time datetime="2012-01-26" pubdate>January 26, 2012</time></div>
            </header>
            <p>I've submitted major updates to Chapter 2 and an all-new chapter on the Blobstore to O'Reilly.  Rough Cuts subscribers should see them at some point in the next week.  RC releases are not fully automatic, so it takes a few days between when I submit it and when it's live on the site.</p>
<p>As I mentioned earlier, for the 2nd edition I'm recommending the Python 2.7 runtime with multithreading enabled for all new Python apps.  The new chapter 2 tutorial reflects this.  I'll be going through the entire book and updating the Python samples for 2.7 and testing with multithreading.  I do not currently plan on including any material in the book about upgrading from Python 2.5, but I could be talked into it.</p>
<p>I've added <a href="http://jinja.pocoo.org/">Jinja2</a> templates to the Python tutorial, and rudimentary JSPs, JSTL, and EL to the Java tutorial.  It's always bothered me that the first example in the book did horrible things like print HTML directly from the handler code.  This also allows me to include larger samples later in the book that rely on some light templating to keep things organized.  I've also updated all of the screenshots in Chapter 2 (which will look hideous in drafts until the art department cleans them up), which doesn't help you that much but makes me feel better.</p>
<p>The Blobstore chapter is mostly written (22 pages in the PDF draft), but there's still a bit left to do.  The chapter will include a complete sample app, in both Python and Java, for accepting, managing, and serving user uploaded files.  Right now, most of the full sample is present for Java, though I'll be reorganizing it.  The equivalent sample for Python is written but isn't placed in the text yet.  I'm planning two short sections on reading from and creating Blobstore values from within the app; right now they're empty headings.</p>
<p>I also set up an empty heading for a new chapter on the Images service.  I omitted the Images service from the 1st edition despite it being available from day one, and nobody has been banging on my door asking for it.  But with the new Blobstore integration, I think it's a cool enough feature to deserve a brief chapter.  The plan is to extend the Blobstore example app with image hosting and thumbnailing features.</p>
<p>But enough about plans.</p>
            
          </article>

          <nav class="recentarticles footboxright">
            <p>Recent articles:</p>
            <ul>
              
              <li><a href="/blog/entry/Quick_Java_datastore_survey__2e_status">Quick Java datastore survey; 2e status</a></li>
              
              <li><a href="/blog/entry/A_Line_in_the_Sand">A Line in the Sand</a></li>
              
              <li><a href="/blog/entry/Writing_an_O_Reilly_Book_Using_Scrivener">Writing an O&#39;Reilly Book Using Scrivener</a></li>
              
              <li class="more"><a href="/blog/entries">more...</a></li>
            </ul>
          </nav>

        </div>
        <div class="sidebox">
          <div class="">
            <p style="text-align: center"><a href="http://oreilly.com/catalog/9780596156732/"><img src="/static/pgae_cover_st.png" width="185" height="243" alt="Programming Google App Engine" border="0" align="center" /></a></p> 
            <p><a href="http://oreilly.com/catalog/9780596522735/"><b><i>Programming Google App Engine</i></b></a> by Dan&nbsp;Sanderson is published by O'Reilly Media, Inc.</p>
          </div>
          <div>
            <p><b><a href="http://oreilly.com/catalog/0636920017547">Preorder the 2nd edition</a></b> and get immediate access to the Rough Cut online. Watch me write it, and help make it better!</p>
          </div>
          <div style="padding: 1.4em 0;">
            <p><b>Get the 1st edition:</b></p>
            <ul>
              <li><a href="http://www.amazon.com/gp/product/059652272X?ie=UTF8&tag=brainlog&linkCode=as2&camp=1789&creative=9325&creativeASIN=059652272X">Paperback</a> or <a href="http://www.amazon.com/gp/product/B003DL3NT8?ie=UTF8&tag=brainlog&linkCode=as2&camp=1789&creative=9325&creativeASIN=B003DL3NT8">Kindle</a> from Amazon.com</li>
              <li><a href="http://oreilly.com/catalog/9780596522735/">PDF + ePub + Mobi + DAISY</a> from O'Reilly</li>
              <li><a href="http://itunes.apple.com/us/app/programming-google-app-engine/id345352599?mt=8">iPhone edition</a> from iTunes</li>
              <li><a href="http://www.amazon.co.jp/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0-Google-App-Engine-Sanderson/dp/4873114756/ref=sr_1_1?ie=UTF8&qid=1305303432&sr=8-1">Japanese translation</a> from Amazon.co.jp</li>
            </ul>
          </div>
          <p><a href="http://www.google.com/profiles/dan.sanderson"><img src="/static/gplus_tiny.png" border="0" style="margin-left: -6px; margin-bottom: -3px;" /></a> <a href="http://www.google.com/profiles/dan.sanderson">Follow dan.sanderson on Google+</a></p>
          <p><a href="http://twitter.com/#!/dan_sanderson"><img src="/static/t_mini-a.png" border="0" /></a> <a href="http://twitter.com/#!/dan_sanderson">Follow @dan_sanderson on Twitter</a></p>
          <p><a href="/blog/atom.xml"><img src="/static/rss_12.png" border="0" width="16" height="16" /></a> <a href="/blog/atom.xml">Subscribe to the news feed</a></p>
        </div>
        <div style="clear: both;"></div>

      </div>
    </div>
    <footer class="outer">
      <div class="innerbox">
        <section class="copyright">
          Copyright &copy; 2009-2012 Dan Sanderson.<br />
          This website is not affiliated with Google Inc. or O'Reilly Media, Inc.<br />
          Google and Google App Engine are trademarks of Google Inc.
        </section>
      </div>
    </footer>
  </body>
</html>
"""