firstnumber, secondnumber = map(int, input().split())
fr = [str(x) for x in str(firstnumber)]
fr = fr[::-1]
fake = [str(x) for x in str(secondnumber)]
fake = fake[::-1]
if ("".join(fr) > ("".join(fake))):
    print("".join(fr))
elif ("".join(fr) < ("".join(fake))):
    print("".join(fake))
elif ("".join(fr) == ("".join(fake))):
    print("".join(fake))
