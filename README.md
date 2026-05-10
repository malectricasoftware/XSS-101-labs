# XSS 101 labs
https://youtu.be/WxIA95JcqU4

## Reflected XSS
by manipulating the name parameter you can cause your javascript to execute due to unsanitized server-side reflection

## Stored XSS
by entering a payload as your username it will be stored and rendered into any posts you submit, resulting in a stored xss vulnerability

## DOM XSS
the client side javascript uses a vulnerable sink without sanitization, resulting in a DOM xss vulnerability  
(you will need to use event handlers to trigger execution as script tags are not generally automatically processed by the browser after a page has already loaded)
