from ciphers.tibia.tibia import encrypted_sentences as tibia_encrypted_sentences
from ciphers.a1z26.a1z26 import encrypted_sentences as a1z26_encrypted_sentences
from ciphers.random_distribution.random_distribution import encrypted_sentences as random_encrypted_sentences
from ciphers.decimalbytes.decimalbytes import encrypted_sentences as decimal_encrypted_sentences
from ciphers.vigenere.vigenere import encrypted_sentences as vigenere_encrypted_sentences

from ciphers.utils.occurences import calculate_data
from ciphers.utils.average import plot_data

# plot_data(calculate_data(a1z26_encrypted_sentences))
# plot_data(calculate_data(decimal_encrypted_sentences))
# plot_data(calculate_data(vigenere_encrypted_sentences))

# plot_data(calculate_data(random_encrypted_sentences))
plot_data(calculate_data(tibia_encrypted_sentences))

   
