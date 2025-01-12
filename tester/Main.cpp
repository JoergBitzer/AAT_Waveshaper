
#include <juce_core/juce_core.h>
#include <juce_audio_basics/juce_audio_basics.h>
#include <juce_audio_processors/juce_audio_processors.h>
#include <juce_dsp/juce_dsp.h>

#include "testsignals.h"
#include "WaveOut.h"

int main()
{
    float samplerate = 44100.f;
    float startfreq = 200.f;
    float endfreq = 20000.f;
    int nrOfSamples = 5*samplerate;

    juce::AudioBuffer<float> buffer;
    buffer.setSize(1,nrOfSamples);
    buffer.clear();

    float* dataptr = buffer.getWritePointer(0);

    genSinusSweep(dataptr,nrOfSamples,startfreq, endfreq,samplerate);

    WaveOut fileout("SweepIn.wav",samplerate,1);
    fileout.write_file(buffer);

    // oversampling
    juce::dsp::Oversampling<float> oversampler(1,2,juce::dsp::Oversampling<float>::filterHalfBandFIREquiripple, true, true);
    oversampler.initProcessing(nrOfSamples);
    juce::dsp::AudioBlock<float> block(buffer);
    auto oversampledAudio = oversampler.processSamplesUp(block);
    auto dataptroversampled = oversampledAudio.getChannelPointer(0);

    int nrofoversampleddata = oversampledAudio.getNumSamples();

    for (int kk = 0; kk < nrofoversampleddata; ++kk)
    {
        float out = 1.5f*dataptroversampled[kk] - 0.5f*dataptroversampled[kk]*dataptroversampled[kk]*dataptroversampled[kk];
        dataptroversampled[kk] = out;
    }

    oversampler.processSamplesDown(block);

    normalizeAudio(buffer,-3.f);

    WaveOut fileout2("SweepOut.wav",samplerate,1);
    fileout2.write_file(buffer);


    return 0;
}