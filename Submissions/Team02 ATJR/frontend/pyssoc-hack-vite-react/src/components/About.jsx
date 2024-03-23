import React from "react";
import { Tilt } from "react-tilt";
import { motion } from "framer-motion";

import { styles } from "../styles";
import { services } from "../constants";

import { fadeIn, textVariant } from "../utils/motion";
import { useInView } from 'react-intersection-observer';


const animateCart = ({ title }) => {
  if (title === "Mass") {
    return { scale: 1.2, y: 100 };
  }
  if (title === "Angular Momentum") {
    return { scale: 1.2, rotate: 360 };
  }
  if (title === "Charge") {
    return {
      scale: 1.8,
      duration: 50,
      boxShadow: "0 0 25px rgba(255, 255, 159, 1)",
    };
  }
  return {};
};

const ServiceCard = ({ index, title, icon }) => (
  <Tilt className="xs:w-[250px] w-full">
    <motion.div
      variants={fadeIn("right", "spring", index * 0.5, 0.75)}
      className="w-full green-pink-gradient p-[1px] rounded-[20px] shadow-card"
      whileHover={animateCart({ title })}
      transition={{ x: -10 }}
    >
      <div
        options={{
          max: 45,
          scale: 1,
          speed: 450,
        }}
        className="bg-tertiary rounded-[20px] py-5 px-12 min-h-[280px] flex justify-evenly items-center flex-col"
      >
        <img
          src={icon}
          alt="black-hole-components"
          className="w-16 h-16 object-contain"
        />

        <h3 className="text-white text-[20px] font-bold text-center">
          {title}
        </h3>
      </div>
    </motion.div>
  </Tilt>
);

const About = () => {
  const {ref, inView} = useInView();
  return (
    <div className="grid justify-items-center">
      <motion.div variants={textVariant()} className="grid justify-items-center">
        <p className={styles.sectionSubText}>Introduction</p>
        <h2 className={styles.sectionHeadText}>Overview.</h2>
      </motion.div>

      <motion.p
        initial={{ opacity: 0, scale: 0.5 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{
          duration: 0.8,
          delay: 0.5,
          ease: [0, 0.71, 0.2, 1.01],
        }}
        className="mt-4 text-secondary text-[17px] max-w-3xl leading-[30px]"
      >
        I am a black hole, the universe's enigma, born from the collapse of a
        massive star. Within my heart lies a singularity, a point where density
        reaches infinity and the laws of physics falter. Encased by my event
        horizon, I am a cosmic point of no return, from which not even light can
        escape.
      </motion.p>

      <motion.p
        initial={{ opacity: 0, scale: 0.5 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{
          duration: 0.8,
          delay: 1,
          ease: [0, 0.71, 0.2, 1.01],
        }}
        className="mt-4 text-secondary text-[17px] max-w-3xl leading-[30px]"
      >
        My existence is marked by the bending of time and space, a gravitational
        pull so strong that it warps the very fabric of the cosmos. I consume
        stars, gas, and cosmic debris, adding their mass to mine, all while
        emitting powerful jets and radiation from the matter swirling at my
        edges, a paradoxical sign of my insatiable hunger.
      </motion.p>

      <motion.p
        ref={ref}
        initial={inView ? { opacity: 0, scale: 0.5 } : {}}
        animate={inView ?  { opacity: 1, scale: 1 } : {}}
        transition={inView ? {
          duration: 0.8,
          delay: 1.5,
          ease: [0, 0.71, 0.2, 1.01],
        }: {}}
        className="mt-4 text-secondary text-[17px] max-w-3xl leading-[30px]"
      >
        To scientists, I am both a mystery and a revelation, holding keys to the
        universe's most profound secrets. I embody the end of some cosmic
        entities and potentially the beginning of new physics, challenging our
        understanding of reality and beckoning us to explore beyond the known.
      </motion.p>

      <div className="mt-20 flex flex-wrap gap-10">
        {services.map((service, index) => (
          <ServiceCard key={service.title} index={index} {...service} />
        ))}
      </div>
    </div>
  );
};

export default About;
