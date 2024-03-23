import React from 'react'
import { motion } from "framer-motion";
import { styles } from "../styles";
import { tableData01 } from '../assets';

const Data = () => {
  return (
    <div className="grid justify-items-center">
      <motion.div className="grid justify-items-center">
        <h2 className={styles.sectionHeadText}>Data</h2>
      </motion.div>
      <img
          src={tableData01}
          alt="black-hole-components"
          className="w-16 h-16 object-contain"
        />
    </div>
  )
}

export default Data