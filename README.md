# PHDoc

PHDoc is a version of Markdoc adapted to the needs of academics.
Markdoc is a project which aims to 
provide a lightweight alternative to large database-powered wiki systems.



## What is it good for?

Potential use cases for PHDoc include, but aren’t limited to:

*   ***Personal* pages in your institution**

    Research institutions usually provide the means
    and expect the researchers
    to create *personal* pages.
    These are usually just a few documents containing the essentials:
    contact information, list of publications
    and maybe a teaching schedule or a list of projects to brag about.
    Most people tend to handcraft static HTML for this,
    as setting up anything dynamic is more pain than gain.
    PHDoc is an easy and efficient alternative.

*   **Quick dissemination of notes, raw data and media objects**

    Perfect for internal communication
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
    
*   **Technical Documentation/Manuals**

    Markdoc can be used to write and render hand-written guides and manuals for
    software. Such documentation will normally be separate from
    automatically-generated API documentation, and might give a higher-level
    view than API docs alone. It might be used for client documentation for
    web/desktop applications, or even developer documentation for frameworks.

*   **Internal Project Wikis**
    
    Markdoc wikis consist of a single plain-text file per page. By combining a
    wiki with a DVCS (such as [Mercurial][] or [Git][]), you can collaborate
    with several other people. Use the DVCS to track, share and merge changes
    with one another, and view the wiki’s history.
    
  [Mercurial]: http://mercurial.selenic.com/
  [Git]: http://git-scm.com/

*   **Static Site Generation**

    Markdoc converts wikis into raw HTML files and media. This allows you to
    manage a blog, personal website or a collection of pages in a Markdoc wiki,
    perhaps with custom CSS styles, and publish the rendered HTML to a website.
    Markdoc need not be installed on the hosting site, since the resultant HTML
    is completely independent.

## Extensions over Markdoc

*   Clean typographic layout, inspired by the beauty of LaTeX-made documents.

*   Automatic hyphenation using Hyphenator by Mathias Nater.

*   LaTeX maths support using MathJax.

*   Foldable quotes support, built specifically for PHDoc.

*   A nice top-bar navigation.

*   Scaffolding with self-explanatory example wiki and configuration.

*   Microsoft Windows support (without remote sync)

*   Rsync your wiki to actually remote locations 
    (using *remote* configuration option)

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

[google analytics]: http://markdoc.org/ref/configuration#metadata
[barebones]: http://markdoc.org/tips/barebones
[pygments]: http://pygments.org/
[syntax-highlighting]: http://markdoc.org/tips/syntax-highlighting
[licensing]: http://markdoc.org/about#license


## Quickstart

### Requirements

The minimum requirements are:

  * Python 2.4 or later (2.5+ highly recommended)
  * A UNIX (or at least POSIX-compliant) operating system
  * [rsync](http://www.samba.org/rsync/) -- installed out of the box with most
    modern OSes, including Mac OS X and Ubuntu. 

### Installation

    $ easy_install phdoc  # OR
    $ pip install phdoc


### Making a Wiki

    phdoc init my-wiki
    cd my-wiki/
    vim wiki/somefile.md
    # ... write some documents ...
    phdoc build
    phdoc serve
    # .. open http://localhost:8008/ in a browser ...

## License

PHDoc is covered by the MIT License:

> Copyright (C) 2013 Remigiusz 'lRem' Modrzejewski
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

The bundled Pygments style (it’s the [Github][] syntax highlighting theme) was
created by [Tom Preston-Werner][]; it was sourced from [his blog][] and is
licensed under the MIT License:

  [github]: http://github.com/
  [tom preston-werner]: http://tom.preston-werner.com/
  [his blog]: http://github.com/mojombo/tpw/

> Copyright © 2010 Tom Preston-Werner
> 
> Permission is hereby granted, free of charge, to any person
> obtaining a copy of this software and associated documentation
> files (the "Software"), to deal in the Software without
> restriction, including without limitation the rights to use,
> copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the
> Software is furnished to do so, subject to the following
> conditions:
> 
> The above copyright notice and this permission notice shall be
> included in all copies or substantial portions of the Software.
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
> EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
> OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
> NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
> HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
> WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
> FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
> OTHER DEALINGS IN THE SOFTWARE.

The bundled [Hyphenator][] library was created by Mathias Nater
and is covered by GNU LGPL:

 
>  Hyphenator 3.3.0 - client side hyphenation for webbrowsers
>  Copyright (C) 2011  Mathias Nater, Zürich (mathias at mnn dot ch)
>  Project and Source hosted on http://code.google.com/p/hyphenator/
> 
>  This JavaScript code is free software: you can redistribute
>  it and/or modify it under the terms of the GNU Lesser
>  General Public License (GNU LGPL) as published by the Free Software
>  Foundation, either version 3 of the License, or (at your option)
>  any later version.  The code is distributed WITHOUT ANY WARRANTY;
>  without even the implied warranty of MERCHANTABILITY or FITNESS
>  FOR A PARTICULAR PURPOSE.  See the GNU GPL for more details.
>
>  As additional permission under GNU GPL version 3 section 7, you
>  may distribute non-source (e.g., minimized or compacted) forms of
>  that code without the copy of the GNU GPL normally required by
>  section 4, provided you include this license notice and a URL
>  through which recipients can access the Corresponding Source.

[Hyphenator]: http://code.google.com/p/hyphenator/
