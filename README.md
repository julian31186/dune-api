# Dune API

## All Endpoints Provided

https://pastebin.com/Hghynju6

## API 

`GET /dune/{term}`

Returns 200 and a response body with a description and wiki link field if the endpoint exists, otherwise will return a 400 error

`GET /dune/ducal_ring`
```
{
    "description": "The Ducal ring was a large signet ring worn as a symbol of office by the Duke of House Atreides.  As seen in the 1984 movie, the ring was an item that Baron Vladimir Harkonnen coveted, swearing that after killing Duke Leto Atreides I, he would have the ring as a trophy.  When Leto Atriedes was poisoned by Wellington Yueh, Yueh took the ring with the intention of giving it to Paul.  Baron Harkonnen was annoyed with Piter de Vries for killing Yueh before finding out where the ring was located.Paul Atreides wore the ring after he and his mother Jessica escaped into the Deep Desert of Arrakis, both as a tribute to his dead father, and as a rallying symbol to the Fremen.The ring itself is ovoid in shape, with a large crimson inset.  The inset carries an impression of the Atreides Coat of Arms.",
    "wiki": "https://dune.fandom.com/wiki/Ducal_ring"
}
```


(Case insensitive)\
(Spaces substituted with underscore '_')

## TODO

- Get random term/name
- Add Quotes
- Write tests