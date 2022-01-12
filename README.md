https://developer.clashofclans.com

# Clash of Clans developer unofficial api Wrapper to generate ip based token

```python
coc  = Coc(email, password)

coc.login()
# generate a new key of your specific ip
key  = coc.createKey("my_ip_address")
# or it will grab your current ip
key  = coc.createKey()
# get all keys
keys  = coc.getAllkeys()

```
