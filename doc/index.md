<!-- title: Index -->

# PHDoc

PHDoc is a version of Markdoc adapted to the needs of academics.
Markdoc is a lightweight Markdown-based wiki system.
It’s been designed to allow
you to create and manage wikis as quickly and easily as possible.


## What is it good for?

Potential use cases for PHDoc include, but aren’t limited to:

*Personal* pages in your institution
:   Research institutions usually provide the means
    and expect the researchers
    to create *personal* pages.
    These are usually just a few documents containing the essentials:
    contact information, list of publications
    and maybe a teaching schedule or a list of projects to brag about.
    Most people tend to handcraft static HTML for this,
    as setting up anything dynamic is more pain than gain.
    PHDoc is an easy and efficient alternative.

Quick dissemination of notes, raw data and media objects
:   Perfect for internal communication
    or dissemination of content that escapes the frame of scientific
    publishing.
    PHDoc allows you to easily write pages containing 
    all the basic HTML markup,
    highlighted code snippets
    and LaTeX mathematics.
    Adding any files,
    be it multimedia or raw data,
    is as simple as putting the files in your directories.
    Directory listings respecting the templates 
    and containing the top-bar navigation
    are created automatically.
    
As well as all that Markdoc is good for:
    
Technical Documentation/Manuals
:   Markdoc can be used to write and render hand-written guides and manuals for
    software. Such documentation will normally be separate from
    automatically-generated API documentation, and might give a higher-level
    view than API docs alone. It might be used for client documentation for
    web/desktop applications, or even developer documentation for frameworks.

Internal Project Wikis
:   Markdoc wikis consist of a single plain-text file per page. By combining a
    wiki with a DVCS (such as [Mercurial][] or [Git][]), you can collaborate
    with several other people. Use the DVCS to track, share and merge changes
    with one another, and view the wiki’s history.
    
  [Mercurial]: http://mercurial.selenic.com/
  [Git]: http://git-scm.com/

Static Site Generation
:   Markdoc converts wikis into raw HTML files and media. This allows you to
    manage a blog, personal website or a collection of pages in a Markdoc wiki,
    perhaps with custom CSS styles, and publish the rendered HTML to a website.
    Markdoc need not be installed on the hosting site, since the resultant HTML
    is completely independent.



## Cool Features

*   Set up [Google Analytics][] tracking in one line of configuration.

*   [Barebones][] wikis that just look like directories with Markdown-formatted
    text files in them.

*   A built-in HTTP server and WSGI application to serve up a compiled wiki with
    a single command.

*   Continuous builds (via `rsync`) mean the server can keep running whilst
    Markdoc re-compiles the wiki. Just refresh your browser to see the changes.

*   Add [Pygments][]-powered syntax highlighting to your Markdoc wiki with a
    single [configuration parameter][syntax-highlighting].

*   Markdoc is [public domain software][licensing]. It will always be completely
    free to use, and you can redistribute it (in part or in whole) under any
    circumstances (open-source, proprietary or otherwise) with no attribution or
    encumberances.

[google analytics]: /ref/configuration#metadata
[barebones]: /tips/barebones
[pygments]: http://pygments.org/
[syntax-highlighting]: /tips/syntax-highlighting
[licensing]: /about#license


## Where do I start?

The [quickstart](/quickstart) document has all the information you need to put
together a simple Markdoc wiki. The [authoring](/authoring) guide provides a
quick introduction to writing Markdoc pages themselves, especially with regards
to linking between pages.


## Reference

See the [configuration](/ref/configuration) reference for in-depth knowledge on
writing your `markdoc.yaml` file. The [layout](/ref/layout) reference describes
the basic filesystem layout for a Markdoc wiki, and the [tips](/tips/) directory
contains several handy recipes.

The Markdoc project’s goals and history are described in the [about](/about)
page. If you’d like to know more about how Markdoc works at a deeper level, take
a look at the [internals directory](/internals/). Developers interested in
hacking the utility will likely want the [development](/internals/development)
page.

To see the complete list of pages in this wiki, you can browse the
[directory listing](/_list).
