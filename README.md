#  Challenge-Handshake Authentication Protocol (CHAP)

CHAP provides protection against replay attacks by the peer through the use of an incrementally changing identifier and of a variable challenge-value. CHAP requires that both the client and server know the plaintext of the secret, although it is never sent over the network. Thus, CHAP provides better security as compared to Password Authentication Protocol (PAP) which is vulnerable for both these reasons. The MS-CHAP variant does not require either peer to know the plaintext and does not transmit it, but has been broken.

# Proof of Concept

![error](https://image-store.slidesharecdn.com/53b716e7-f899-4024-8514-d523ba0bae93-original.png)
