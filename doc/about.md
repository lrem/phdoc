# About PHDoc

PHDoc is a version of Markdoc adapted to the needs of academics.
Markdoc is a project which aims to 
provide a lightweight alternative to large database-powered wiki systems.


## Goals & Philosophy

### Wikis

*   Wikis should be made up of plain-text files, without requiring a running
    instance of MySQL or even an SQLite database.

*   There should only be one simple-to-write plain-text configuration file.

*   Wikis should be VCS-friendly, yet VCS-agnostic.

*   It should be possible to compile a wiki to static HTML, and then to serve
    this HTML with no wiki-specific software.


### Markdown

I chose Markdown as the format for this wiki system because of its simplicity,
familiarity for many writers, and the extensibility of its Python
implementation. For example, Pygments syntax highlighting is available through a
single configuration option in the `markdoc.yaml` file. The ability to embed raw
HTML in Markdown documents gives it power and flexibility.


### Command-Line Interface

*   The CLI should be intuitive and easy to use.

*   There should only be a few different sub-commands, each of which does what
    one would expect it to.

*   There should be a full web server included, in the case that setting up a
    large-scale HTTP server is impractical or impossible.

*   The CLI should be pure-Python, for portability and extensibility.


## Extensions over Markdoc

*   Clean typographic layout, inspired by the beauty of LaTeX-made documents.

*   Automatic hyphenation using Hyphenator by Mathias Nater.

*   LaTeX maths support using MathJax.

*   Foldable quotes support using, built for PHDoc.

*   A nice top-bar navigation.

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
